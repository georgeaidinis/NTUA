-- This file contains the SQL code for the creation and
-- establishment of views for the non-updateable version
-- of our database.

USE database;


-- -----------------------------------------------------
-- Author view. Hides the AuthorID column from the user
-- -----------------------------------------------------

CREATE VIEW Authors_view AS
	select Authors.Name, Authors.Surname, Authors.Birthdate
	from Authors;



-- -----------------------------------------------------
-- Authored view. Hides the AuthorID column from the user
-- and provides Author Name, Surname, and the books he/she
-- has authored via the ISBN and Title.
-- -----------------------------------------------------

CREATE VIEW Authored_view AS
	select Authors.Name, Authors.Surname, Books.ISBN, Books.Title
	from  Authors, Books, Authored
	where Authored.Authors_AuthorID = Authors.AuthorID and Authored.Books_ISBN = Books.ISBN
	group by Authors.Surname, Authors.Name;


-- -----------------------------------------------------
-- Member view. Hides the MemberID column from the user
-- -----------------------------------------------------

CREATE VIEW Members_view AS
	select Members.Name,Members.Surname,Members.Birthdate
	from Members;

CREATE VIEW Books_view AS
	select *
	from Books;

CREATE VIEW Publishers_view AS
	select *
	from Publishers;

CREATE VIEW Copies_view AS
	select *
	from Copy;
