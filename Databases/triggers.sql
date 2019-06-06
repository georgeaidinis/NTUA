use `database`;
create table if not exists `database`.`myerror`(
	`T` bool not null default 1,
	`F` bool not null default 0,
	primary key (`T`) )
Engine = InnoDB;


-- 1. den mporei na yparksei ekdotis me imerominia idryseos megaliteri apo thn shmerinh
delimiter $$
create trigger check_pub_date_of_est
	before insert 
    on Publishers for each row
begin
	if new.Date_of_Establishment > year(curdate() ) then
		insert into myerror(T)
        values (null);
	end if;
end$$
delimiter ;

-- 2. den mporei na yparksei monimo melos pou den exei hdh kataxorithei os melos
delimiter $$
create trigger check_perm_staff_attr
	before insert 
    on Permanent for each row
begin
    if ( new.Hiring_Date > curdate() + interval 1 month or not exists (select * from Staff where Staff.StaffID = new.Staff_StaffID) ) then
		insert into myerror(T) values (null) ;
	end if;
end$$
delimiter ;

-- 3. borrowing check
delimiter $$
create trigger update_borrowed_num
after insert
	on Borrows for each row
begin
	-- -- --
    -- update num_books_borrowed, if latter < 5 after update do nothing more
    -- -- --
	if( (select num_books_borrowed from Members where Members.MemberID = new.Members_MemberID ) < 4) then
		update Members
			set Members.num_books_borrowed = Members.num_books_borrowed + 1
			where Members.MemberID = new.Members_MemberID;
	-- -- --
    -- -- if new val of num_books_borrowed = 5, change Can_Borrow to false
    -- -- --
    elseif ( (select num_books_borrowed from Members where Members.MemberID = new.Members_MemberID ) > 4 or exists (select * from Members where Members.MemberID = new.Members_MemberID and Members.Can_Borrow = False)) then
		insert into myerror(T)
			values(null);
	else 
		update Members
			set Members.num_books_borrowed = Members.num_books_borrowed + 1, Members.Can_Borrow = False
			where Members.MemberID = new.Members_MemberID;
	end if;
end$$
delimiter ;

-- 4. return check
delimiter $$
create trigger return_book
after update
	on Borrows for each row
begin
	-- -- --
	-- decrease member s num_books_borrowed by 1
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
    -- check whether given member s borrowing are due
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

-- 5. update borrowing ability
delimiter $$
create trigger update_borrowing_ability
after insert on Reminds for each row
begin
	if exists( select * from Borrows where Borrows.Members_MemberID = new.Members_MemberID 
										and curdate() > Borrows.Due_Date and Borrows.Return_date is null ) 
	then
		update Members
        set Members.Can_Borrow = false
        where Members.MemberID = new.Members_MemberID;
    end if;
	
end$$
delimiter ;

-- 6. make sure publisher is registered before book is inserted
delimiter $$
create trigger check_publisher_registered
	before insert on Books for each row
begin
    if not exists ( select * from Publishers where Publishers.Name = new.Publishers_Name ) then
		insert into Publishers(Name)
        values(new.Publishers_Name);	
    end if;
end$$
delimiter ;

-- 7. if all copies of a book are deleted, delete the book
delimiter $$
create trigger all_copies_deleted
	after delete
	on Copy for each row
begin
	if not exists (select * from Copy where Copy.Books_ISBN = OLD.Books_ISBN) then
		delete from Books
			where Books.ISBN = OLD.Books_ISBN;
	end if;
end$$
delimiter ;


-- 8. if no copy of inserted book is registered, add one
delimiter $$
create trigger insert_copy
	after insert on Books for each row
begin
	if not exists( select * from Copy where Copy.Books_ISBN = new.ISBN) then
	insert into Copy(Books_ISBN, Number, Position)
		values (new.ISBN, 1, NULL);

	end if;
end$$
delimiter ;

-- 9. insert author if author does not exists
delimiter $$
create trigger unknown_author
	after insert on Books for each row
begin 

	if not exists( select * from Authors where Authors.Name = new.AuthorName and Authors.Surname = new.AuthorSur ) then
	insert into Authors (Name,Surname)
		values (new.AuthorName, new.AuthorSur);
	end if;
    
	if not exists( select * from Authored where Authored.Books_ISBN = new.ISBN ) then 
--     insert
-- 		select new.ISBN, AuthorsID into Authors_Books_ISBN,Authros_AuthorID 
-- 			from Authors where Authors.Name = new.AuthorName and Authors.Surname = new.AuthorSur ;
	insert into Authored ( Books_ISBN, Authors_AuthorID )
		select new.ISBN, AuthorID from Authors where (Authors.Name = new.AuthorName and Authors.Surname = new.AuthorSur );
	end if; 
end$$
delimiter ;

-- -- 10. book has valid date
delimiter $$
create trigger valid_pub_date
	before insert on Books for each row
begin
	if new.Publication_Year > year(curdate()) then
	insert into myerror(T)
		values(null);
	end if;

end$$
delimiter ;

-- --11. one cannot borrow a copy that is already borrowed and not returned
delimiter $$
create trigger copy_is_avail
	before insert on Borrows for each row
begin
	if exists (select * from Borrows where Borrows.Copy_Books_ISBN = new.Copy_Books_ISBN 
    and Borrows.Copy_Number = new.Copy_Number 
    and Borrows.Return_date is null) then
		insert into myerror(T)
        values(null);
	end if;
end$$
delimiter ;

-- --12. before inserting borrowing, check user is allowed to
delimiter $$
create trigger check_user_can_borrow
	before insert on Borrows for each row
begin
	if exists(select * from Members where Members.Can_Borrow = 0 and Members.MemberID = new.Members_MemberID) then
		insert into myerror(T)
		values(null);
	end if;
end$$
delimiter ;