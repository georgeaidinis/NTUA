USE database;

select *
from Books
where Books.Pages>1400;


select *
FROM Members
where YEAR(CURDATE()) - YEAR(birthdate) > 27;