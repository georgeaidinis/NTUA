structure Cmap = BinaryMapFn(struct
				type ord_key = int*int
				fun compare((x1,y1),(x2,y2)) =
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

	fun readGrid (y,arr,cats,water,i:int,j:int,n,m) =
		case y of NONE => (arr,cats,water,n,m-1,0)
		| SOME(#" ") => readGrid(TextIO.input1 inStream,arr,cats,water,i,j,n,m)
		| SOME(#"\n") => readGrid(TextIO.input1 inStream,arr,cats,water,i+1,0,max(n,i),max(m,j))
		| SOME(#"A") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),(#"A",0)),pf(cats,i,j,0),water,i,j+1,max(n,i),max(m,j))
		| SOME(#"W") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),(#"W",0)),cats,pf(water,i,j,0),i,j+1,max(n,i),max(m,j))
		| SOME(#".") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),(#".",0)),cats,water,i,j+1,max(n,i),max(m,j))
		| SOME(#"X") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),(#"X",0)),cats,water,i,j+1,max(n,i),max(m,j))
		| _ => (arr,cats,water,n,m-1,0)

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

	fun update_c(arr,cats,water,i:int,j:int,c:char,t:int,n:int,m:int) =
	let
		val	 x = Cmap.find(arr,(i,j))
		val  y = 0
	in
	case c of #"R" =>
	if j<=n andalso x = #"." then update_c(Cmap.insert(arr,(i,j),(c,t+1)),pf(cats,(i,j)),water,i,j-2,#"L",t,n,m)
	else if j<=n andalso is_cat(x) andalso y = t+1 then update_c(Cmap.insert(arr,(i,j),(conflict(c,x),t+1)),cats,water,i,j-2,#"L",t,n,m)
	else update_c(arr,cats,water,i,j-2,#"L",t,n,m)
	| #"L" =>
	if j>=0 andalso x = #"." then update_c(Cmap.insert(arr,(i,j),(c,t+1)),pf(cats,(i,j)),water,i+1,j+1,#"U",t,n,m)
	else if j>=0 andalso is_cat(x) andalso y = t+1 then update_c(Cmap.insert(arr,(i,j),(conflict(c,x),t+1)),cats,water,i+1,j+1,#"U",t,n,m)
	else update_c(arr,cats,water,i+1,j+1,#"U",t,n,m)
	| #"U" =>
	if i>=0 andalso x = #"." then update_c(Cmap.insert(arr,(i,j),(c,t+1)),pf(cats,(i,j)),water,i-1,j,#"D",t,n,m)
	else if i>=0 andalso is_cat(x) andalso y = t+1 then update_c(Cmap.insert(arr,(i,j),(conflict(c,x),t+1)),cats,water,i-1,j,#"D",t,n,m)
	else update_c(arr,cats,water,i-1,j,#"D",t,n,m)
	| #"D" =>
	if i<=m andalso x = #"." then update_cat(Cmap.insert(arr,(i,j),(c,t+1)),pf(cats,(i,j)),water,t,n,m)
	else if i<=m andalso is_cat(x) andalso y = t+1 then update_cat(Cmap.insert(arr,(i,j),(conflict(c,x),t+1)),cats,water,t,n,m)
	else update_cat(arr,cats,water,t,n,m)
	end

	and update_cat (arr,cats,water,t:int,n:int,m:int) =
	let
		val (i,j,s) = Queue.dequeue(cats)
	in
		case s-t of 1 => update_water(arr,pf(cats,i,j,s),water,t,n,m)
		| _ => update_c(arr,cats,water,i,j+1,#"R",t,n,m)
	end

	and update_w(arr,cats,water,i:int,j:int,c:char,t:int,n:int,m:int) =
	let
		val (x,y) = Cmap.find(arr,(i,j))
	in
	case c of #"R" =>
	if j<=n andalso x = #"." then update_w(Cmap.insert(arr,(i,j),(#"W",t+1)),cats,pf(water,(i,j)),i,j-2,#"L",t,n,m)
	else if j<=n andalso is_cat(x) andalso y = t+1 then update_w(Cmap.insert(arr,(i,j),(kill(x),t+1)),cats,water,i,j-2,#"L",t,n,m)
	else update_w(arr,cats,water,i,j-2,#"L",t,n,m)
	| #"L" =>
	if j>=0 andalso x = #"." then update_c(Cmap.insert(arr,(i,j),(#"W",t+1)),cats,pf(water,(i,j)),i+1,j+1,#"U",t,n,m)
	else if j>=0 andalso is_cat(x) andalso y = t+1 then update_c(Cmap.insert(arr,(i,j),(kill(x),t+1)),cats,water,i+1,j+1,#"U",t,n,m)
	else update_w(arr,cats,water,i+1,j+1,#"U",t,n,m)
	| #"U" =>
	if i>=0 andalso x = #"." then update_c(Cmap.insert(arr,(i,j),(#"W",t+1)),cats,pf(water,(i,j)),i-2,j,#"D",t,n,m)
	else if i>=0 andalso is_cat(x) andalso y = t+1 then update_c(Cmap.insert(arr,(i,j),(kill(x),t+1)),cats,water,i-2,j,#"D",t,n,m)
	else update_w(arr,cats,water,i-2,j,#"D",t,n,m)
	| #"D" =>
	if i<=m andalso x = #"." then update_cat(Cmap.insert(arr,(i,j),(#"W",t+1)),cats,pf(water,(i,j)),t,n,m)
	else if i<=m andalso is_cat(x) andalso y = t+1 then update_cat(Cmap.insert(arr,(i,j),(kill(x),t+1)),cats,water,t,n,m)
	else update_water(arr,cats,water,t,n,m)
	end

	and update_water(arr,cats,water,t:int,n:int,m:int) =
	let
		val (i,j,s) = Queue.dequeue(cats)
	in
		case s-t of 1 => answer(arr,pf(cats,i,j,s),water,n,m,t)
		| _ => update_w(arr,cats,water,i,j+1,#"R",t,n,m)
	end

	and answer (arr,cats,water,n:int,m:int,t:int) =
	if t <> 1
		then
			case (Queue.isEmpty(cats),Queue.isEmpty(water)) of (true,true) => print("infinity")
			| _ => answer(update_cat(arr,cats,water,n,m-1,t))
	else (Cmap.find(arr,(1,1)))
	in
		answer(readGrid(TextIO.input1 inStream,Cmap.empty,Queue.mkQueue(),Queue.mkQueue(),0,0,0,0))
end
