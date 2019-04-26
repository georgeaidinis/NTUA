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
            case y of NONE => (arr,time_array,cats,water,1,n,m,1,0,water_num,0)
            | SOME(#" ") => readGrid(TextIO.input1 inStream,arr,time_array,cats,water,i,j,n,m,water_num)
            | SOME(#"\n") => readGrid(TextIO.input1 inStream,arr,time_array,cats,water,i+1,0,n+1,max(m,j),water_num)
            | SOME(#"A") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"A"),Cmap.insert(time_array,(i,j),0),pf(cats,i,j,0),water,i,j+1,n,m,water_num)
            | SOME(#"W") => readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"W"),Cmap.insert(time_array,(i,j),0),cats,pf(water,i,j,0),i,j+1,n,m,water_num+1)
            | SOME(#".") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"."),Cmap.insert(time_array,(i,j),0),cats,water,i,j+1,n,m,water_num)
            | SOME(#"X") =>	readGrid(TextIO.input1 inStream,Cmap.insert(arr,(i,j),#"X"),Cmap.insert(time_array,(i,j),0),cats,water,i,j+1,n,m,water_num)
            | _ => (arr,time_array,cats,water,1,n,m,1,0,water_num,0)

        fun conflict(x,y) =
            if x>y then x
            else y

        fun is_cat (x) =
            case x of #"A" => true
            | #"L" => true
            | #"U" => true
            | #"D" => true
            | #"R" => true
            | _ => false

        fun were_cat (x) =
            case x of #"a" => true
            | #"l" => true
            | #"u" => true
            | #"d" => true
            | #"r" => true
            | _ => false

        fun kill (x) = Char.chr(Char.ord x + Char.ord#"a" - Char.ord#"A")
        fun revive (x) = Char.chr(Char.ord x - Char.ord#"a" + Char.ord#"A")

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
                        | _ => update_cat(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
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
                    | _ => update_cat(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)

        and update_cat (arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev) =
            if Queue.isEmpty(cats) andalso cats_num<>0 then update_water(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
            else if Queue.isEmpty(cats) andalso cats_num=0 then answer(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
            else
            let
                    val (i,j,time) = Queue.dequeue(cats)
                in
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
                        | _ =>  update_water(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
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
                    | _ => update_water(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)

        and update_water(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev) =
            if Queue.isEmpty(water) then answer(arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev)
            else
                let
                    val (i,j,time) = Queue.dequeue(water)
                in
                    case time-t of 1 => answer(arr,time_array,cats,pf(water,i,j,time),t,n,m,cats_num,cats_prev,water_num,water_prev)
                    | _ => update_w(arr,time_array,cats,water,i,j+1,#"R",t,n,m,cats_num,cats_prev,water_num,water_prev)

                end

        (*
        fun find_time (*...*)
        fun ananeothikan_nera (*...*)
        *)
        and help (arr,i,j,n,m) =
            if i<=n-1 andalso j<m-1 then (Int.toString(valOf(Cmap.find(arr,(i,j)))) ^ " " ^ help(arr,i,j+1,n,m))
            else if i<n-1 andalso j=m-1 then (Int.toString(valOf(Cmap.find(arr,(i,j)))) ^ " \n" ^ help(arr,i+1,0,n,m))
            else Int.toString(valOf(Cmap.find(arr,(i,j)))) ^ " \n"

        and str_answer(arr,i,j,str) =
            let
                val c = Char.toString(valOf(Cmap.find(arr,(i,j))))
            in
                case c of "R" => str_answer(arr,i,j-1,str) ^ "R"
                | "r" =>  str_answer(arr,i,j-1,str) ^ "R"
                | "L" => str_answer(arr,i,j+1,str) ^ "L"
                | "l" => str_answer(arr,i,j+1,str) ^ "L"
                | "U" => str_answer(arr,i+1,j,str) ^ "U"
                | "u" => str_answer(arr,i+1,j,str) ^ "U"
                | "D" => str_answer(arr,i-1,j,str) ^ "D"
                | "d" => str_answer(arr,i-1,j,str) ^ "D"
                | "A" => str
                | "a" => str
                | _ => str
        end
        and george_is_stupid(arr,time_array,i,j,n,m,t) =
            let
                val x = valOf(Cmap.find(arr,(i,j)))
            in
                if were_cat(x) andalso valOf(Cmap.find(time_array,(i,j))) = t then (i,j)
                else if i<=n-1 andalso j<m-1 then george_is_stupid(arr,time_array,i,j+1,n,m,t)
                else if i<n-1 andalso j=m-1 then george_is_stupid(arr,time_array,i+1,0,n,m,t)
                else (i,j)
                end

        and find_last_pos (arr,time_array,i,j,n,m,best_i,best_j) =
            let
                val x = valOf(Cmap.find(arr,(i,j)))
                val y = valOf(Cmap.find(time_array, (i,j)))
            in
                if i<=n-1 andalso j<m-1 then
                    if is_cat(revive(x)) then
                        if (valOf(Cmap.find(time_array,(i,j))) = valOf(Cmap.find(time_array,(best_i,best_j)))) then
                            if      (i<best_i) then find_last_pos(arr,time_array,i,j+1,n,m,i,j)
                            else if (i=best_i) andalso (j<best_j) then find_last_pos(arr,time_array,i,j+1,n,m,best_i,j)
                            else find_last_pos(arr,time_array,i,j+1,n,m,best_i,best_j)
                        else if (valOf(Cmap.find(time_array,(i,j))) > valOf(Cmap.find(time_array,(best_i,best_j)))) then
                            find_last_pos(arr,time_array,i,j+1,n,m,i,j)
                        else find_last_pos(arr,time_array,i,j+1,n,m,best_i,best_j)
                    else find_last_pos(arr,time_array,i,j+1,n,m,best_i,best_j)
                else if i<n-1 andalso j=m-1 then
                    if is_cat(revive(x)) then
                        if (valOf(Cmap.find(time_array,(i,j))) = valOf(Cmap.find(time_array,(best_i,best_j)))) then
                            if      (i<best_i) then find_last_pos(arr,time_array,i+1,0,n,m,i,j)
                            else if (i=best_i) andalso (j<best_j) then find_last_pos(arr,time_array,i+1,0,n,m,best_i,j)
                            else find_last_pos(arr,time_array,i+1,0,n,m,best_i,best_j)
                        else if (valOf(Cmap.find(time_array,(i,j))) > valOf(Cmap.find(time_array,(best_i,best_j)))) then
                            find_last_pos(arr,time_array,i+1,0,n,m,i,j)
                        else find_last_pos(arr,time_array,i+1,0,n,m,best_i,best_j)
                    else find_last_pos(arr,time_array,i+1,0,n,m,best_i,best_j)
                else
                    if is_cat(revive(x)) then
                        if (valOf(Cmap.find(time_array,(i,j))) > valOf(Cmap.find(time_array,(best_i,best_j)))) then (i,j)
                        else (best_i,best_j)
                    else (best_i,best_j)

            end

        and find_first_pos (arr,i,j,n,m) =
        if i<=n-1 andalso j<m-1 then
            if is_cat(valOf(Cmap.find(arr,(i,j)))) then (i,j)
            else find_first_pos (arr,i,j+1,n,m)
        else if i<n-1 andalso j=m-1 then
            if is_cat(valOf(Cmap.find(arr,(i,j)))) then (i,j)
            else find_first_pos (arr,i+1,0,n,m)
        else (i,j)

        and answer (arr,time_array,cats,water,t,n,m,cats_num,cats_prev,water_num,water_prev) =
            (*...*)
            if cats_num = cats_prev andalso Queue.isEmpty(cats) andalso water_prev = water_num then print("infinity"^ "\n"^answer_Inf(arr,n,m)^"\n")
            else if Queue.isEmpty(cats) andalso cats_num = 0 then
                    print (Int.toString(t-1)^"\n"^answer_Ninf(arr,time_array,n,m,t)^"\n")
            (*print xrono, kiniseis *)
            else update_cat(arr, time_array,cats, water, t+1, n, m,cats_num,cats_num,water_num,water_num)

            and answer_Inf(arr,n,m) =
                let
                    val (i,j) = find_first_pos(arr,0,0,n,m)
                    val str = str_answer(arr,i,j,"")
                in
                    case str of "" => "stay"
                    | _ => str
                end

            and answer_Ninf(arr,time_array,n,m,t) =
            let
                val (i,j) = george_is_stupid(arr,time_array,0,0,n,m,t)
                val str = str_answer(arr,i,j,"")
            in
                case str of "" => "stay"
                | _ => str
            end
        in
                update_cat(readGrid(TextIO.input1 inStream,Cmap.empty,Cmap.empty,Queue.mkQueue(),Queue.mkQueue(),0,0,0,0,0))
end
        
