
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
	