structure Cmap = BinaryMapFn(struct
				type ord_key = int
				fun compare(x,y) = 
				if x<y then LESS else if x>y then GREATER else EQUAL
			end)

fun colors fileName =
	let
		fun parse file =
			let
				(* A function to read an integer from specified input. *)
				fun readInt input =
					Option.valOf (TextIO.scanStream (Int.scan StringCvt.DEC) input)
				(* Open input file. *)
				val inStream = TextIO.openIn file

				(* Read an integer (number of countries) and consume newline. *)
				val n = readInt inStream
				val k = readInt inStream
				val _ = TextIO.inputLine inStream

				(* A function to read N integers from the open file. *)
				fun readInts 0 acc = rev acc (* Replace with 'rev acc' for proper order. *)
				  | readInts i acc = readInts (i - 1) (readInt inStream :: acc)
			in
				(n,k, readInts n [])
			end
		fun colors_solution(n:int,k:int,l:int list) =
			let
				fun addnode(ar,nodekey:int) =
					if Cmap.find(ar,nodekey) = NONE then Cmap.insert(ar,nodekey,1) 
					else Cmap.insert(ar,nodekey,valOf(Cmap.find(ar,nodekey))+1)

				fun removenode(ar,nodekey:int) =
					let 
						val (x,y) = Cmap.remove(ar,nodekey)
					in
						if (y = 1) then x
						else Cmap.insert(x,nodekey,y-1)
					end

				fun add(curr,ar,ans:int,n:int,k:int,length:int,l:int list) =
						(*if l = [1,3,1,3,1,3,3,2,2,1] then (curr,ar,ans,n,k,(tl l)) *)
						let
							val y = Queue.enqueue(curr,hd l)
						in
							(curr,addnode(ar,(hd l)),ans,n,k,length+1,(tl l))
						end

				fun rem(curr,ar,ans:int,n:int,k:int,length:int,l:int list) =
					(curr,removenode(ar,Queue.dequeue(curr)),ans,n,k,length-1,l)

				fun min(ans:int,length:int) =
					if length<ans then length
					else ans

				fun cr(curr,ar,ans:int,n:int,k:int,length:int,l:int list) =			
					if Cmap.numItems(ar) < k andalso l <> [] then cr(add(curr,ar,ans,n,k,length,l))
					else if Cmap.numItems(ar) = k then cr(rem(curr,ar,min(ans,length),n,k,length,l))
					else if (ans=n+1) then print("0\n")
					else print(Int.toString(ans)^"\n")

					val ans = n+1
					val ar = Cmap.empty
					val curr = Queue.mkQueue()		
			in
				cr(curr,ar,ans,n,k,0,l)
			end
	in
		colors_solution (parse fileName)
end
