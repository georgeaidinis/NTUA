DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  password varchar(255) DEFAULT NULL,
  username varchar(255) UNIQUE DEFAULT NULL,
  role int(1) DEFAULT 0,
  daily_quotas int(3) DEFAULT 50,
  email varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
);