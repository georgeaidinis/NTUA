-- -- -- -- -- -- --
-- -- -- triggers --
-- -- -- -- -- -- --


-- -- --
-- trigger for books getting borrowed
-- -- --
use `database`;
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
	else
		update Members
			set Members.num_books_borrowed = Members.num_books_borrowed + 1, Members.Can_Borrow = False
			where Members.MemberID = new.Members_MemberID;
	end if;
end$$
delimiter ;

-- -- --
-- trigger for books getting returned
-- -- --
use `database`;
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

-- -- --
-- trigger for the borrowing ability of members
-- -- --
use `database`;
delimiter $$;
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