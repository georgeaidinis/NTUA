USE database;



-- ---------------------------------
-- Borrows Relation:
-- ---------------------------------

INSERT INTO Borrows VALUES (1,1,"101-1312-1148","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (1,1,"101-1312-9808","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (1,1,"101-1312-4486","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (2,2,"101-1312-1148","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (2,1,"101-1312-1643","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (2,1,"101-1312-9050","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (3,3,"101-1312-1148","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (3,2,"101-1312-9050","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (3,1,"101-1312-9096","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (4,4,"101-1312-1148","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (4,3,"101-1312-9050","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (4,2,"101-1312-9096","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (5,5,"101-1312-1148","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (5,4,"101-1312-9050","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (5,3,"101-1312-9096","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (6,2,"101-1312-9808","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (6,5,"101-1312-9050","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (6,1,"101-1312-9050","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (7,1,"101-1312-9552","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (7,1,"101-1312-9951","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (7,1,"101-1312-6363","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (9,1,"101-1312-4065","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (9,2,"101-1312-9951","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (9,1,"101-1312-8033","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (8,3,"101-1312-9951","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (8,2,"101-1312-8033","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (8,1,"101-1312-1643","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (10,4,"101-1312-9951","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (10,2,"101-1312-9808","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (10,3,"101-1312-9808","2019-01-01",null, "2019-02-01");

INSERT INTO Borrows VALUES (11,5,"101-1312-9951","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (11,6,"101-1312-9951","2019-01-01",null, "2019-02-01");
INSERT INTO Borrows VALUES (11,7,"101-1312-9951","2019-01-01",null, "2019-02-01");



-- ---------------------------------
-- Category Relation:
-- ---------------------------------
INSERT INTO Category VALUES ("Romance", "Romance");
INSERT INTO Category VALUES ("Horror", "Horror");
INSERT INTO Category VALUES ("Philosophical", "Philosophical");
INSERT INTO Category VALUES ("Modern History", "Modern History");
INSERT INTO Category VALUES ("Global History", "Global History");
INSERT INTO Category VALUES ("Comedy", "Comedy");
INSERT INTO Category VALUES ("Drama", "Drama");
INSERT INTO Category VALUES ("Social", "Social");
INSERT INTO Category VALUES ("Science", "Science");
INSERT INTO Category VALUES ("Mystery", "Mystery");
INSERT INTO Category VALUES ("Political", "Political");
INSERT INTO Category VALUES ("Sci-fiy", "Sci-fi");
INSERT INTO Category VALUES ("Fiction", "Fiction");
INSERT INTO Category VALUES ("Art", "Art");




INSERT INTO Category VALUES ("Romance", "Horror");
INSERT INTO Category VALUES ("Horror", "Philosophical");
INSERT INTO Category VALUES ("Philosophical", "Modern History");
INSERT INTO Category VALUES ("Modern History", "Global History");
INSERT INTO Category VALUES ("Comedy", "Drama");
INSERT INTO Category VALUES ("Social", "Political");
INSERT INTO Category VALUES ("Political", "Comedy");
INSERT INTO Category VALUES ("Sci-fi", "Science");
INSERT INTO Category VALUES ("Fiction", "Philosophical");
INSERT INTO Category VALUES ("Mystery", "Drama");
INSERT INTO Category VALUES ("Poetry", "Art");




-- ---------------------------------
-- Belongs Relation:
-- ---------------------------------


INSERT INTO Belongs VALUES ("101-1312-2133","Romance");
INSERT INTO Belongs VALUES ("960-418-059-2","Horror");
INSERT INTO Belongs VALUES ("101-1312-4486","Philosophical");
INSERT INTO Belongs VALUES ("07-060229-8","Modern History");
INSERT INTO Belongs VALUES ("960-8129-06-0","Comedy");
INSERT INTO Belongs VALUES ("960-418-087-8","Drama");
INSERT INTO Belongs VALUES ("9789604614486","Social");
INSERT INTO Belongs VALUES ("960-7510-05-4","Political");
INSERT INTO Belongs VALUES ("960-7643-18-6","Sci-fi");
INSERT INTO Belongs VALUES ("101-1312-2179","Comedy");
INSERT INTO Belongs VALUES ("978-960-411-715-4","Science");
INSERT INTO Belongs VALUES ("978-960-546-692-3","Science");
INSERT INTO Belongs VALUES ("101-1312-8461","Science");
INSERT INTO Belongs VALUES ("960-7530-32-2","Science");
INSERT INTO Belongs VALUES ("960-7225-13-9","Drama");
INSERT INTO Belongs VALUES ("101-1312-1148","Art");
INSERT INTO Belongs VALUES ("101-1312-2100","Poetry");
INSERT INTO Belongs VALUES ("101-1312-4015","Mystery");
INSERT INTO Belongs VALUES ("978-960-266-058-4","Mystery");
INSERT INTO Belongs VALUES ("101-1312-3993","Fiction");
INSERT INTO Belongs VALUES ("960-8250-12-9","Comedy");
INSERT INTO Belongs VALUES ("960-254-649-2","Comedy");
INSERT INTO Belongs VALUES ("960-254-659-X","Romance");




-- ---------------------------------
-- Reminds Relation:
-- ---------------------------------


INSERT INTO Reminds VALUES (1,12,null);
INSERT INTO Reminds VALUES (1,16,null);
INSERT INTO Reminds VALUES (1,19,null);
INSERT INTO Reminds VALUES (1,21,null);
INSERT INTO Reminds VALUES (2,6,null);
INSERT INTO Reminds VALUES (3,18,null);
INSERT INTO Reminds VALUES (2,17,null);
INSERT INTO Reminds VALUES (3,2,null);
INSERT INTO Reminds VALUES (2,1,null);
INSERT INTO Reminds VALUES (3,10,null);
INSERT INTO Reminds VALUES (2,9,null);
INSERT INTO Reminds VALUES (2,12,null);
INSERT INTO Reminds VALUES (3,13,null);
INSERT INTO Reminds VALUES (4,20,null);
INSERT INTO Reminds VALUES (4,2,null);
INSERT INTO Reminds VALUES (4,5,null);
INSERT INTO Reminds VALUES (4,11,null);
INSERT INTO Reminds VALUES (4,23,null);
INSERT INTO Reminds VALUES (4,18,null);
INSERT INTO Reminds VALUES (4,16,null);
INSERT INTO Reminds VALUES (4,20,null);
INSERT INTO Reminds VALUES (4,23,null);
INSERT INTO Reminds VALUES (4,24,null);


-- ---------------------------------
-- Permanent Relation:
-- ---------------------------------

INSERT INTO Permanent VALUES (4,"2017-01-20");
INSERT INTO Permanent VALUES (5,"2017-01-20");
INSERT INTO Permanent VALUES (6,"2017-01-20");
INSERT INTO Permanent VALUES (7,"2017-01-20");
INSERT INTO Permanent VALUES (8,"2017-01-20");
INSERT INTO Permanent VALUES (9,"2017-01-20");




-- ---------------------------------
-- Temporary Relation:
-- ---------------------------------

INSERT INTO Temporary VALUES (1,1);
INSERT INTO Temporary VALUES (2,1);
INSERT INTO Temporary VALUES (3,1);
