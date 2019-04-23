structure Cmap = BinaryMapFn(struct
				type ord_key = int * int
				fun compare ((x1,y1),(x2,y2)) =
				if x1<x2 then LESS else if x1>x2 then GREATER else if y1<y2 then LESS else if y1>y2 then GREATER else EQUAL
			end)


fun parse file =
	let
		(* A function to read an integer from specified input. *)
		(* Open input file. *)
	val inStream = TextIO.openIn file

	fun max(a,b) =
		if a<b then b
		else a

	fun pf(a,i,j,t) =
	let
		val y = Queue.enqueue(a,(i,j,t))
	in
		a
	end

	fun readGrid (y,arr,time_array,cats,water,i:int,j:int,n,m) =
		case y of NONE => (arr,time_array,cats,water,n,m-1,0)
		| SOME(#" ") => readGrid(TextIO.input1 inStream,arr,time_array,cats,water,i,j,n,m)
		| SOME(#"\n") => readGrid(TextIO.input1 inStream,arr,time_array,cats,water,i+1,0,max(n,i),max(m,j))
		| SOME(#"A") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"A"),Cmap.insert(time_array,(i,j),0),pf(cats,i,j,0),pf(water,i,j,0),i,j+1,max(n,i),max(m,j))
		| SOME(#"W") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array,(i,j),0),pf(cats,i,j,0),pf(water,i,j,0),i,j+1,max(n,i),max(m,j))
		| SOME(#".") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"."),Cmap.insert(time_array,(i,j),0),pf(cats,i,j,0),pf(water,i,j,0),i,j+1,max(n,i),max(m,j))
		| SOME(#"X") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"X"),Cmap.insert(time_array,(i,j),0),pf(cats,i,j,0),pf(water,i,j,0),i,j+1,max(n,i),max(m,j))
		| _ => (arr,time_array,cats,water,n,m-1,0)

	fun conflict(x,y) =
		if x>y then x
		else y

	fun is_cat (x) =
	case x of #"A" => true
	| #"L" => true
	| #"D" => true
	| #"U" => true
	| #"R" => true
	| _ => false

	fun kill (x) = Char.chr(Char.ord x + Char.ord#"a" - Char.ord#"A")

	fun update_c(arr,time_array,cats,water,i:int,j:int,c:char,t:int,n:int,m:int) =
	let
		val	x = Cmap.find(arr,(i,j))
		val	y = 0
	in
	case c of #"R" =>
	if j<=n andalso valOf(x) = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array,(i,j),t+1),pf(cats,i,j,t),water,i,j-2,#"L",t,n,m)
	else if j<=n andalso is_cat(valOf(x)) andalso y = t+1 then update_c(Cmap.insert(arr,(i,j),conflict(c,valOf(x))),Cmap.insert(time_array,(i,j),t+1),cats,water,i,j-2,#"L",t,n,m)
	else update_c(arr,time_array,cats,water,i,j-2,#"L",t,n,m)
	| #"L" =>
	if j>=0 andalso valOf(x) = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t+1),pf(cats,i,j,t),water,i+1,j+1,#"U",t,n,m)
	else if j>=0 andalso is_cat(valOf(x)) andalso y = t+1 then update_c(Cmap.insert(arr,(i,j),conflict(c,valOf(x))),Cmap.insert(time_array, (i,j), t+1),cats,water,i+1,j+1,#"U",t,n,m)
	else update_c(arr,time_array,cats,water,i+1,j+1,#"U",t,n,m)
	| #"U" =>
	if i>=0 andalso valOf(x) = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array,(i,j),t+1),pf(cats,i,j,t),water,i-1,j,#"D",t,n,m)
	else if i>=0 andalso is_cat(valOf(x)) andalso y = t+1 then update_c(Cmap.insert(arr,(i,j),conflict(c,valOf(x))),Cmap.insert(time_array,(i,j),t+1),cats,water,i-1,j,#"D",t,n,m)
	else update_c(arr,time_array,cats,water,i-1,j,#"D",t,n,m)
	| #"D" =>
	if i<=m andalso valOf(x) = #"." then update_cat(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array,(i,j),t+1),pf(cats,i,j,t),water,t,n,m)
	else if i<=m andalso is_cat(valOf(x)) andalso y = t+1 then update_cat(Cmap.insert(arr,(i,j),conflict(c,valOf(x))),Cmap.insert(time_array,(i,j),t+1),cats,water,t,n,m)
	else update_cat(arr,time_array,cats,water,t,n,m)
	end

	and update_cat (arr,time_array,cats,water,t:int,n:int,m:int) =
	let
		val (i,j,s) = Queue.dequeue(cats)
	in
		case s-t of 1 => update_water(arr,time_array,pf(cats,i,j,s),water,t,n,m)
		| _ => update_c(arr,time_array,cats,water,i,j+1,#"R",t,n,m)
	end

	and update_w(arr,time_array,cats,water,i:int,j:int,c:char,t:int,n:int,m:int) =
	let
		val x = Cmap.find(arr,(i,j))
		val y = Cmap.find(time_array,(i,j))
	in
	case c of #"R" =>
	if j<=n andalso valOf(x) = #"." then update_w(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t+1),cats,pf(cats,i,j,t),i,j-2,#"L",t,n,m)
	else if j<=n andalso is_cat(valOf(x)) andalso valOf(y) = t+1 then update_w(Cmap.insert(arr,(i,j),kill(valOf(x))),Cmap.insert(time_array, (i,j),t+1),cats,water,i,j-2,#"L",t,n,m)
	else update_w(arr,time_array,cats,water,i,j-2,#"L",t,n,m)
	| #"L" =>
	if j>=0 andalso valOf(x) = #"." then update_c(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t+1),cats,pf(cats,i,j,t),i+1,j+1,#"U",t,n,m)
	else if j>=0 andalso is_cat(valOf(x)) andalso valOf(y) = t+1 then update_c(Cmap.insert(arr,(i,j),kill(valOf(x))),Cmap.insert(time_array, (i,j),t+1),cats,water,i+1,j+1,#"U",t,n,m)
	else update_w(arr,time_array,cats,water,i+1,j+1,#"U",t,n,m)
	| #"U" =>
	if i>=0 andalso valOf(x) = #"." then update_c(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t+1),cats,pf(cats,i,j,t),i-2,j,#"D",t,n,m)
	else if i>=0 andalso is_cat(valOf(x)) andalso valOf(y) = t+1 then update_c(Cmap.insert(arr,(i,j),kill(valOf(x))),Cmap.insert(time_array, (i,j),t+1),cats,water,i-2,j,#"D",t,n,m)
	else update_w(arr,time_array,cats,water,i-2,j,#"D",t,n,m)
	| #"D" =>
	if i<=m andalso valOf(x) = #"." then update_cat(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t+1),cats,pf(cats,i,j,t),t,n,m)
	else if i<=m andalso is_cat(valOf(x)) andalso valOf(y) = t+1 then update_cat(Cmap.insert(arr,(i,j),kill(valOf(x))),Cmap.insert(time_array, (i,j),t+1),cats,water,t,n,m)
	else update_water(arr,time_array,cats,water,t,n,m)
	end

	and update_water(arr,time_array,cats,water,t:int,n:int,m:int) =
	let
		val (i,j,s) = Queue.dequeue(cats)
	in
		case s-t of 1 => answer(arr,time_array,pf(cats,i,j,s),water,n,m,t)
		| _ => update_w(arr,time_array,cats,water,i,j+1,#"R",t,n,m)
	end

	and answer (arr,time_array,cats,water,n:int,m:int,t:int) =
	if t <> 1
		then
			case (Queue.isEmpty(cats),Queue.isEmpty(water)) of (true,true) => print("infinity")
			| _ => answer(update_cat(arr,time_array,cats,water,n,m-1,t))
	else (Cmap.find(arr,(1,1)))
	in
		answer(readGrid(TextIO.input1 inStream,Cmap.empty,Cmap.empty,Queue.mkQueue(),Queue.mkQueue(),0,0,0,0))
end












