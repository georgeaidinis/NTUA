structure Cmap = BinaryMapFn(struct
				type ord_key = int * int
				fun compare ((x1,y1),(x2,y2)) =
				if x1<x2 then LESS else if x1>x2 then GREATER else if y1<y2 then LESS else if y1>y2 then GREATER else EQUAL
			end)


fun savethecat file =
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

		fun readGrid (y,arr,time_array,cats,water,i:int,j:int,n,m,water_num) =
<<<<<<< HEAD
			case y of NONE => (arr,time_array,cats,water,1,n+1,m,1,0,water_num,0)
			| SOME(#" ") => readGrid(TextIO.input1 inStream,arr,time_array,cats,water,i,j,n,m,water_num)
			| SOME(#"\n") => readGrid(TextIO.input1 inStream,arr,time_array,cats,water,i+1,0,n+1,max(m,j),water_num)
			| SOME(#"A") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"A"),Cmap.insert(time_array,(i,j),0),pf(cats,i,j,0),water,i,j+1,n,m,water_num)
			| SOME(#"W") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array,(i,j),0),cats,pf(water,i,j,0),i,j+1,n,m,water_num+1)
			| SOME(#".") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"."),Cmap.insert(time_array,(i,j),0),cats,water,i,j+1,n,m,water_num)
			| SOME(#"X") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"X"),Cmap.insert(time_array,(i,j),0),cats,water,i,j+1,n,m,water_num)
			| _ => (arr,time_array,cats,water,1,n+1,m,1,0	,water_num,0)

		fun conflict(x,y) =
			if x>y then x
=======
			case y of NONE => (arr,time_array,cats,water,1,n,m-1,1,water_num,0)
			| SOME(#" ") => readGrid(TextIO.input1 inStream,arr,time_array,cats,water,i,j,n,m,water_num)
			| SOME(#"\n") => readGrid(TextIO.input1 inStream,arr,time_array,cats,water,i+1,0,max(n,i),max(m,j),water_num)
			| SOME(#"A") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"A"),Cmap.insert(time_array,(i,j),0),pf(cats,i,j,0),water,i,j+1,max(n,i),max(m,j),water_num)
			| SOME(#"W") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array,(i,j),0),cats,pf(water,i,j,0),i,j+1,max(n,i),max(m,j),water_num+1)
			| SOME(#".") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"."),Cmap.insert(time_array,(i,j),0),cats,water,i,j+1,max(n,i),max(m,j),water_num)
			| SOME(#"X") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"X"),Cmap.insert(time_array,(i,j),0),cats,water,i,j+1,max(n,i),max(m,j),water_num)
			| _ => (arr,time_array,cats,water,1,n,m-1,1,water_num,0)

		fun conflict(x,y) =
			if x<y then x
>>>>>>> 275dc5e0cdde130778d8516e81b4d724dcef1a76
			else y

		fun is_cat (x) =
		case x of #"A" => true
		| #"L" => true
<<<<<<< HEAD
		| #"U" => true
		| #"D" => true
=======
		| #"D" => true
		| #"U" => true
>>>>>>> 275dc5e0cdde130778d8516e81b4d724dcef1a76
		| #"R" => true
		| _ => false

		fun kill (x) = Char.chr(Char.ord x + Char.ord#"a" - Char.ord#"A")

<<<<<<< HEAD
		fun update_c(arr,time_array,cats,water,i:int,j:int,c:char,t,n,m,cats_num,cats_prev,water_num,water_prev) =
			if j<m andalso j>=0 andalso i<n andalso i>=0 then
					let
						val	x = valOf(Cmap.find(arr,(i,j)))
						val	y = valOf(Cmap.find(time_array, (i,j)))
					in
						case c of #"R" =>
							if x = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t),pf(cats,i,j,t+1),water,i,j-2,#"L",t,n,m,cats_num+1,cats_prev,water_num,water_prev)
							else if  is_cat(x) andalso y = t then update_c(Cmap.insert(arr,(i,j),conflict(c,x)),time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,cats_prev,water_num,water_prev)
						else update_c(arr,time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,cats_prev,water_num,water_prev)
						| #"L" =>
							if  x = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t),pf(cats,i,j,t+1),water,i+1,j+1,#"D",t,n,m,cats_num+1,cats_prev,water_num,water_prev)
							else if is_cat(x) andalso y = t then update_c(Cmap.insert(arr,(i,j),conflict(c,x)),time_array,cats,water,i+1,j+1,#"D",t,n,m,cats_num,cats_prev,water_num,water_prev)
							else update_c(arr,time_array,cats,water,i+1,j+1,#"D",t,n,m,cats_num,cats_prev,water_num,water_prev)
						| #"D" =>
							if  x = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t),pf(cats,i,j,t+1),water,i-2,j,#"U",t,n,m,cats_num+1,cats_prev,water_num,water_prev)
							else if  is_cat(x) andalso y = t then update_c(Cmap.insert(arr,(i,j),conflict(c,x)),time_array,cats,water,i-2,j,#"U",t,n,m,cats_num,cats_prev,water_num,water_prev)
							else update_c(arr,time_array,cats,water,i-2,j,#"U",t,n,m,cats_num,cats_prev,water_num,water_prev)
						| #"U" =>
							if  x = #"." then update_cat(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t),pf(cats,i,j,t+1),water,t,n,m,cats_num+1,cats_prev,water_num,water_prev)
							else if  is_cat(x) andalso y = t then update_cat(Cmap.insert(arr,(i,j),conflict(c,x)),time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
							else update_cat(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
					end
			else
					case c of #"R" =>
						update_c(arr,time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,cats_prev,water_num,water_prev)
					| #"L" =>
						update_c(arr,time_array,cats,water,i+1,j+1,#"D",t,n,m,cats_num,cats_prev,water_num,water_prev)
					| #"D" =>
						update_c(arr,time_array,cats,water,i-2,j,#"U",t,n,m,cats_num,cats_prev,water_num,water_prev)
					| #"U" =>
						update_cat(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)

		and update_cat (arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev) =
			if Queue.isEmpty(cats) andalso cats_num<>0 then update_water(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
			else if Queue.isEmpty(cats) andalso cats_num=0 then answer(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
=======
		fun update_c(arr,time_array,cats,water,i:int,j:int,c:char,t,n,m,cats_num,water_num,water_prev) =
			if j<=m andalso j>=0 andalso i<=n andalso i>=0 then
				let
					val	x = valOf(Cmap.find(arr,(i,j)))
					val	y = valOf(Cmap.find(time_array, (i,j)))
				in
					case c of #"R" =>
						if x = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t),pf(cats,i,j,t+1),water,i,j-2,#"L",t,n,m,cats_num+1,water_num,water_prev)
						else if  is_cat(x) andalso y = t then update_c(Cmap.insert(arr,(i,j),conflict(c,x)),time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,water_num,water_prev)
					else update_c(arr,time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,water_num,water_prev)
					| #"L" =>
						if  x = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t),pf(cats,i,j,t+1),water,i+1,j-1,#"U",t,n,m,cats_num+1,water_num,water_prev)
						else if is_cat(x) andalso y = t then update_c(Cmap.insert(arr,(i,j),conflict(c,x)),time_array,cats,water,i+1,j-1,#"U",t,n,m,cats_num,water_num,water_prev)
						else update_c(arr,time_array,cats,water,i+1,j-1,#"U",t,n,m,cats_num,water_num,water_prev)
					| #"U" =>
						if  x = #"." then update_c(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t),pf(cats,i,j,t+1),water,i+2,j,#"D",t,n,m,cats_num+1,water_num,water_prev)
						else if  is_cat(x) andalso y = t then update_c(Cmap.insert(arr,(i,j),conflict(c,x)),time_array,cats,water,i+2,j,#"D",t,n,m,cats_num,water_num,water_prev)
						else update_c(arr,time_array,cats,water,i+2,j,#"D",t,n,m,cats_num,water_num,water_prev)
					| #"D" =>
						if  x = #"." then update_cat(Cmap.insert(arr,(i,j),c),Cmap.insert(time_array, (i,j),t),pf(cats,i,j,t+1),water,t,n,m,cats_num+1,water_num,water_prev)
						else if  is_cat(x) andalso y = t then update_cat(Cmap.insert(arr,(i,j),conflict(c,x)),time_array,cats,water,t,n,m,cats_num,water_num,water_prev)
						else update_cat(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev)
				end
			else
			case c of #"R" =>
				update_c(arr,time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,water_num,water_prev)
			| #"L" =>
				update_c(arr,time_array,cats,water,i+1,j-1,#"U",t,n,m,cats_num,water_num,water_prev)
			| #"U" =>
				update_c(arr,time_array,cats,water,i+2,j,#"D",t,n,m,cats_num,water_num,water_prev)
			| #"D" =>
				update_cat(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev)

		and update_cat (arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev) =
			if Queue.isEmpty(cats) andalso cats_num<>0 then update_water(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev)
			else if Queue.isEmpty(cats) andalso cats_num=0 then answer(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev)
>>>>>>> 275dc5e0cdde130778d8516e81b4d724dcef1a76
			else
			let
					val (i,j,time) = Queue.dequeue(cats)
				in
<<<<<<< HEAD
					if (is_cat(valOf(Cmap.find(arr,(i,j))))) then
						case time-t of 1 =>  update_water(arr,time_array,pf(cats,i,j,time),water,t,n,m,cats_num,cats_prev,water_num,water_prev)
						| _ =>  update_c(arr,time_array,cats,water,i,j+1,#"R",t,n,m,cats_num,cats_prev,water_num,water_prev)
					else update_cat(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
				end




		and update_w(arr,time_array,cats,water,i:int,j:int,c:char,t,n,m,cats_num,cats_prev,water_num,water_prev) =
			if j<m andalso j>=0 andalso i<n andalso i>=0 then
					let
						val x = valOf(Cmap.find(arr,(i,j)))
						val y = valOf(Cmap.find(time_array,(i,j)))
					in
						case c of #"R" =>
							if x = #"." then update_w(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i,j-2,#"L",t,n,m,cats_num,cats_prev,water_num+1,water_prev)
							else if is_cat(x) then update_w(Cmap.insert(arr,(i,j),kill(x)),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i,j-2,#"L",t,n,m,cats_num-1,cats_prev,water_num+1,water_prev)
							else update_w(arr,time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,cats_prev,water_num,water_prev)
						| #"L" =>
							if x = #"." then update_w(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i+1,j+1,#"D",t,n,m,cats_num,cats_prev,water_num+1,water_prev)
							else if is_cat(x) then update_w(Cmap.insert(arr,(i,j),kill(x)),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i+1,j+1,#"D",t,n,m,cats_num-1,cats_prev,water_num+1,water_prev)
							else update_w(arr,time_array,cats,water,i+1,j+1,#"D",t,n,m,cats_num,cats_prev,water_num,water_prev)
						| #"D" =>
							if x = #"." then update_w(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i-2,j,#"U",t,n,m,cats_num,cats_prev,water_num+1,water_prev)
							else if is_cat(x) then update_c(Cmap.insert(arr,(i,j),kill(x)),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i-2,j,#"U",t,n,m,cats_num-1,cats_prev,water_num+1,water_prev)
							else update_w(arr,time_array,cats,water,i-2,j,#"U",t,n,m,cats_num,cats_prev,water_num,water_prev)
						| #"U" =>
							if x = #"." then update_water(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),t,n,m,cats_num,cats_prev,water_num+1,water_prev)
							else if is_cat(x) then update_water(Cmap.insert(arr,(i,j),kill(x)),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),t,n,m,cats_num-1,cats_prev,water_num+1,water_prev)
							else update_water(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
					end
			else
					case c of #"R" =>
						update_w(arr,time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,cats_prev,water_num,water_prev)
					| #"L" =>
						update_w(arr,time_array,cats,water,i+1,j+1,#"D",t,n,m,cats_num,cats_prev,water_num,water_prev)
					| #"D" =>
						update_w(arr,time_array,cats,water,i-2,j,#"U",t,n,m,cats_num,cats_prev,water_num,water_prev)
					| #"U" =>
						update_water(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)

		and update_water(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev) =
			if Queue.isEmpty(water) then answer(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
			else
				let
					val (i,j,time) = Queue.dequeue(water)
				in
					case time-t of 1 => answer(arr,time_array,cats,pf(water,i,j,time),t,n,m,cats_num,cats_prev,water_num,water_prev)
					| _ => update_w(arr,time_array,cats,water,i,j+1,#"R",t,n,m,cats_num,cats_prev,water_num,water_prev)

				end
=======
					case time-t of 1 => update_water(arr,time_array,pf(cats,i,j,time),water,t,n,m,cats_num,water_num,water_prev) 						| _ => update_c(arr,time_array,cats,water,i,j+1,#"R",t,n,m,cats_num,water_num,water_prev)
				end

		and update_w(arr,time_array,cats,water,i:int,j:int,c:char,t,n,m,cats_num,water_num,water_prev) =
			if j<=m andalso j>=0 andalso i<=n andalso i>=0 then
			let
				val x = valOf(Cmap.find(arr,(i,j)))
				val y = valOf(Cmap.find(time_array,(i,j)))
			in
				case c of #"R" =>
					if x = #"." then update_w(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i,j-2,#"L",t,n,m,cats_num,water_num+1,water_num)
					else if is_cat(x) then update_w(Cmap.insert(arr,(i,j),kill(x)),time_array,cats,pf(water,i,j,t+1),i,j-2,#"L",t,n,m,cats_num-1,water_num+1,water_num)
					else update_w(arr,time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,water_num,water_prev)
				| #"L" =>
					if x = #"." then update_w(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i-1,j+1,#"U",t,n,m,cats_num,water_num+1,water_num)
					else if is_cat(x) then update_w(Cmap.insert(arr,(i,j),kill(x)),time_array,cats,pf(water,i,j,t+1),i-1,j+1,#"U",t,n,m,cats_num-1,water_num+1,water_num)
					else update_w(arr,time_array,cats,water,i+1,j+1,#"U",t,n,m,cats_num,water_num,water_prev)
				| #"U" =>
					if x = #"." then update_w(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),i+2,j,#"D",t,n,m,cats_num,water_num+1,water_num)
					else if is_cat(x) then update_c(Cmap.insert(arr,(i,j),kill(x)),time_array,cats,pf(water,i,j,t+1),i+2,j,#"D",t,n,m,cats_num-1,water_num+1,water_num)
					else update_w(arr,time_array,cats,water,i-2,j,#"D",t,n,m,cats_num,water_num,water_prev)
				| #"D" =>
					if x = #"." then update_water(Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array, (i,j),t),cats,pf(water,i,j,t+1),t,n,m,cats_num,water_num+1,water_num)
					else if is_cat(x) then update_water(Cmap.insert(arr,(i,j),kill(x)),time_array,cats,pf(water,i,j,t+1),t,n,m,cats_num-1,water_num+1,water_num)
					else update_water(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev)
			end
			else 
			case c of #"R" =>
				update_w(arr,time_array,cats,water,i,j-2,#"L",t,n,m,cats_num,water_num,water_prev)
			| #"L" =>
				update_w(arr,time_array,cats,water,i+1,j+1,#"D",t,n,m,cats_num,water_num,water_prev)
			| #"D" =>
				update_w(arr,time_array,cats,water,i-2,j,#"U",t,n,m,cats_num,water_num,water_prev)
			| #"U" =>
				update_water(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev)

		and update_water(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev) =
			if Queue.isEmpty(water) andalso Queue.isEmpty(cats) then answer(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev)
			else if Queue.isEmpty(water) then answer(arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev)
			else 
				let
					val (i,j,time) = Queue.dequeue(water)
				in
					case time-t of 1 => answer(arr,time_array,cats, pf(water,i,j,time),t,n,m,cats_num,water_num,water_prev)
					| _ => update_w(arr,time_array,cats,water,i,j+1,#"R",t,n,m,cats_num,water_num,water_prev)
	
				end	
>>>>>>> 275dc5e0cdde130778d8516e81b4d724dcef1a76

		(*
		fun find_time (*...*)
		fun ananeothikan_nera (*...*)
		*)
<<<<<<< HEAD


		and help (arr,i,j,n,m) =
			if i<=n-1 andalso j<m-1 then (Int.toString(valOf(Cmap.find(arr,(i,j)))) ^ " " ^ help(arr,i,j+1,n,m))
			else if i<n-1 andalso j=m-1 then (Int.toString(valOf(Cmap.find(arr,(i,j)))) ^ " \n" ^ help(arr,i+1,0,n,m))
			else Int.toString(valOf(Cmap.find(arr,(i,j)))) ^ " \n"

		and answer (arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev) =
			(*...*)
			if cats_num = cats_prev andalso Queue.isEmpty(cats) andalso water_prev = water_num then print("Cats are safe\n"^"Time:"^Int.toString(t-1)^",cats_num:"^Int.toString(cats_num)^",water_num:"^Int.toString(water_num)^",water_prev:"^Int.toString(water_prev) ^ "\n" ^ help(time_array,0,0,n,m))
			else if Queue.isEmpty(cats) andalso cats_num = 0 then
					print ( "Cats_num = 0" ^ "   time:"^Int.toString(t-1)^",cats_num:"^Int.toString(cats_num)^",water_num:"^Int.toString(water_num)^",water_prev:"^Int.toString(water_prev)^ "\n" ^ help(time_array,0,0,n,m))
			(*print xrono, kiniseis *)
			else if Queue.isEmpty(cats) andalso water_num = water_prev then
					print ( "Prev = current"^ "   time:"^Int.toString(t-1)^",cats_num:"^Int.toString(cats_num)^",water_num:"^Int.toString(water_num)^",water_prev:"^Int.toString(water_prev)^ "\n" ^ help(time_array,0,0,n,m))
				else update_cat(arr, time_array,cats, water, t+1, n, m,cats_num,cats_num,water_num,water_num)
			(*else print(Char.toString(valOf(Cmap.find(arr, (4,4)))))*)
		(*
			else print("hi,"^Int.toString(t-1)^","^Int.toString(cats_num)^","^Int.toString(water_num)^","^Int.toString(water_prev))
			*)
		in
				update_cat(readGrid(TextIO.input1 inStream,Cmap.empty,Cmap.empty,Queue.mkQueue(),Queue.mkQueue(),0,0,0,0,0))
=======
		and answer (arr,time_array,cats,water,t,n,m,cats_num,water_num,water_prev) =
			(*...*)
			if Queue.isEmpty(cats) andalso cats_num = 0 then
					print("Cats_num = 0" ^ "   time:"^Int.toString(t-1)^",cats_num:"^Int.toString(cats_num)^",water_num:"^Int.toString(water_num)^",water_prev:"^Int.toString(water_prev))
			(*print xrono, kiniseis *)
			else if Queue.isEmpty(cats) andalso water_num = water_prev then
					print("Prev = current"^ "   time:"^Int.toString(t-1)^",cats_num:"^Int.toString(cats_num)^",water_num:"^Int.toString(water_num)^",water_prev:"^Int.toString(water_prev))
			else if t<=14 then  update_cat(arr, time_array, cats, water, t+1, n, m,cats_num,water_num,water_prev)
			else print(Char.toString(valOf(Cmap.find(arr, (4,4)))))
		(*
			else print("hi,"^Int.toString(t-1)^","^Int.toString(cats_num)^","^Int.toString(water_num)^","^Int.toString(water_prev))
			*)

	in
		update_cat(readGrid(TextIO.input1 inStream,Cmap.empty,Cmap.empty,Queue.mkQueue(),Queue.mkQueue(),0,0,0,0,0))
>>>>>>> 275dc5e0cdde130778d8516e81b4d724dcef1a76
end

(* an oura gates einai mideniki
	an oi gates einai miden sto tablo	}	kalese tin synartisi exoume teleiwsei peta xrono-3, print string twn thesewn
	or den exoun ananeothei ta nera		}*)
