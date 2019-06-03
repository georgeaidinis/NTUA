use `database`;

insert into Authored (Authors_AuthorID, Books_ISBN )
( select AuthorID, ISBN from Books 
INNER JOIN Authors 
ON ( Books.AuthorName = Authors.Name AND Books.AuthorSur = Authors.Surname) );