-- use `database`;
-- select AuthorSur from Books;
-- 
-- select * from Authors;

--  select Authors.* from Books 
--  RIGHT JOIN Authors 
--  ON ( Books.AuthorName = Authors.Name AND Books.AuthorSur = Authors.Surname);
--  
--  insert into Authored (Authors_AuthorID, Books_ISBN )
--  ( select AuthorID, ISBN from Books 
--  INNER JOIN Authors 
--  ON ( Books.AuthorName = Authors.Name AND Books.AuthorSur = Authors.Surname) );
-- 


-- select * from Authored;
-- select * from Copy order by Books_ISBN;
-- select * from Category;

-- -- -- -- -- -- --
-- -- triggers --
-- -- -- -- -- -- --
drop trigger update_borrowed_num;
-- drop trigger return_book;
delimiter $$
create trigger update_borrowed_num
after insert
	on Borrows for each row
begin
	if( (select num_books_borrowed from Members where Members.MemberID = new.Members_MemberID ) < 4) then
		update Members
			set Members.num_books_borrowed = Members.num_books_borrowed + 1
			where Members.MemberID = new.Members_MemberID;
	else
		update Members
			set Members.num_books_borrowed = Members.num_books_borrowed + 1, Members.Can_Borrow = False
			where Members.MemberID = new.Members_MemberID;
	end if;
end$$
delimiter ;

-- delimiter $$
-- create trigger return_book
-- after update
-- 	on Borrows for each row
-- begin
-- 	if ( (select num_books_borrowed from Members where Members.MemberID = new.Members_MemberID) = 5 
-- 			and exists( * from Members where (Members.MemberID = new.Members_MemberID and ) ) ) 
-- 	then 
-- 		update Members
-- 			set Members.num_books_borrowed = Members.num_books_borrowed - 1, set Members.Can_Borrow = True
-- 			where Members.MemberID = new.Members_MemberID;
-- 	else if
--     else
--     if 
--     update Members
-- 			set Members.num_books_borrowed = Members.num_books_borrowed - 1, set Members.Can_Borrow = True
-- 			where Members.MemberID = new.Members_MemberID;
--     
-- end$$
-- delimiter ;
-- 
drop trigger return_book;

delimiter $$
create trigger return_book
after update
	on Borrows for each row
begin
	-- -- --
	-- decrease member's num_books_borrowed by 1
    -- -- --
	update Members
		set Members.num_books_borrowed = Members.num_books_borrowed - 1
        where Members.MemberID = new.Members_MemberID;
        
	-- -- --
    -- if num_books_borrowed of giver member was 5 make Can_Borrow true
    -- -- --
	if ((select Members.num_books_borrowed from Members where Members.MemberID = new.Members_MemberID) = 4)
	then
        update Members
			set Members.Can_Borrow = True
            where Members.MemberID = new.Members_MemberID;
    end if;
    
	-- -- --
    -- check whether given member's borrowing are due
    -- -- --
    if exists( select * from Borrows where Borrows.Members_MemberID = new.Members_MemberID 
												and Borrows.Due_Date >= curdate()
												and Borrows.Return_date is null)
	then
		update Members
			set Members.Can_Borrow = False
            where Members.MemberID = new.Members_MemberID;
	end if;
end$$
delimiter ;


-- ()INSERT INTO
-- select * from Staff;
-- select * from Members;
-- update Members
-- set Can_Borrow = 1 where MemberID = 1;
-- select * from Members where MemberID = 1;
-- select count(t.Publishers_Name) from (select Publishers_Name from 
-- Books inner join Publishers
-- on Books.Publishers_Name = Publishers.Name) as t;
-- 
-- select count(*) from Books;
-- select sum(num) from (select count(*) as num from Copy group by Books_ISBN ) as t;-- 