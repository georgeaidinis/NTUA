-- Πεμ 23 Μαΐ 2019 03:13:13 μμ EEST
-- Model: New Model    Version: 1.0

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

-- -----------------------------------------------------
-- Schema database
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema database
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `database` DEFAULT CHARACTER SET utf8 ;
USE `database` ;

-- -----------------------------------------------------
-- Table `database`.`Publishers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Publishers` (
  `Name` VARCHAR(60) NOT NULL,
  `Address` VARCHAR(60) NULL,
  `Date_of_Establishment` INT NULL,
  PRIMARY KEY (`Name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Library`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Library` (
  `LibraryName` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`LibraryName`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Books` (
  `ISBN` VARCHAR(18) NOT NULL,
  `Title` VARCHAR(160) NULL,
  `Pages` INT NULL,
  `Publication_Year` INT NULL,
  `Publishers_Name` VARCHAR(60) NOT NULL,
  `LibraryName` VARCHAR(10) NOT NULL,
  `AuthorName` VARCHAR(80) NOT NULL,
  `AuthorSur` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`ISBN`),
  INDEX `fk_Books_Publishers1_idx` (`Publishers_Name` ASC),
  CONSTRAINT `fk_Books_Publishers1`
    FOREIGN KEY (`Publishers_Name`)
    REFERENCES `database`.`Publishers` (`Name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Books_Library1`
    FOREIGN KEY (`LibraryName`)
    REFERENCES `database`.`Library` (`LibraryName`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Authors` (
  `AuthorID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(60) NULL,
  `Surname` VARCHAR(60) NULL,
  `Birthdate` INT NULL,
  PRIMARY KEY (`AuthorID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Members`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Members` (
  `MemberID` INT NOT NULL AUTO_INCREMENT,
  `Birthdate` DATE NULL,
  `Address` VARCHAR(60) NULL,
  `Name` VARCHAR(60) NULL,
  `Surname` VARCHAR(60) NULL,
  `num_books_borrowed` INT NULL,
  `Can_Borrow`  TINYINT(1) NOT NULL,
  `LibraryName` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`MemberID`),
  CONSTRAINT `fk_Members_Library1`
    FOREIGN KEY (`LibraryName`)	
    REFERENCES `database`.`Library` (`LibraryName`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Staff` (
  `StaffID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(60) NULL,
  `Pay` INT NULL,
  `Surname` VARCHAR(60) NULL,
  `LibraryName` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`StaffID`),
  CONSTRAINT `fk_Staff_Library`
    FOREIGN KEY (`LibraryName`)
    REFERENCES `database`.`Library` (`LibraryName`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Category` (
  `Name` VARCHAR(60) NOT NULL,
  `Parent_category` VARCHAR(60) NULL,
  PRIMARY KEY (`Name`),
  INDEX `fk_Category_Category1_idx` (`Parent_category` ASC),
  CONSTRAINT `fk_Category_Category1`
    FOREIGN KEY (`Parent_category`)
    REFERENCES `database`.`Category` (`Name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Copy`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Copy` (
  `Books_ISBN` VARCHAR(18) NOT NULL,
  `Number` INT NOT NULL,
  `Position` VARCHAR(10) NULL,
  PRIMARY KEY (`Books_ISBN`, `Number` ),
  CONSTRAINT `fk_Copy_Books1`
    FOREIGN KEY (`Books_ISBN`)
    REFERENCES `database`.`Books` (`ISBN`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Temporary`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Temporary` (
  `Staff_StaffID` INT NOT NULL,
  `ContractID` INT NOT NULL,
  PRIMARY KEY (`Staff_StaffID`),
  INDEX `fk_Temporary_Staff1_idx` (`Staff_StaffID` ASC),
  CONSTRAINT `fk_Temporary_Staff1`
    FOREIGN KEY (`Staff_StaffID`)
    REFERENCES `database`.`Staff` (`StaffID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Permanent`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Permanent` (
  `Staff_StaffID` INT NOT NULL,
  `HIring Date` DATE NOT NULL,
  PRIMARY KEY (`Staff_StaffID`),
  INDEX `fk_Permanent_Staff1_idx` (`Staff_StaffID` ASC),
  CONSTRAINT `fk_Permanent_Staff1`
    FOREIGN KEY (`Staff_StaffID`)
    REFERENCES `database`.`Staff` (`StaffID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Borrows`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Borrows` (
  `Members_MemberID` INT NOT NULL,
  `Copy_Number` INT NOT NULL,
  `Copy_Books_ISBN` VARCHAR(18) NOT NULL,
  `Start_Date` DATE NULL,
  `Return_date` DATE NULL,
  `Due_Date` DATE NULL,
  PRIMARY KEY (`Members_MemberID`, `Copy_Books_ISBN`, `Copy_Number`),
  INDEX `fk_Members_has_Copy_Copy1_idx` (`Copy_Books_ISBN` ASC, `Copy_Number` ASC ),
  INDEX `fk_Members_has_Copy_Members1_idx` (`Members_MemberID` ASC),
  CONSTRAINT `fk_Membexrs_has_Copy_Members1`
    FOREIGN KEY (`Members_MemberID`)
    REFERENCES `database`.`Members` (`MemberID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Members_has_Copy_Copy1`
    FOREIGN KEY ( `Copy_Books_ISBN`,`Copy_Number`)
    REFERENCES `database`.`Copy` ( `Books_ISBN`, `Number` )
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Belongs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Belongs` (
  `Books_ISBN` VARCHAR(18) NOT NULL,
  `Category_Name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Books_ISBN`, `Category_Name`),
  INDEX `fk_Books_has_Category_Category1_idx` (`Category_Name` ASC),
  INDEX `fk_Books_has_Category_Books1_idx` (`Books_ISBN` ASC),
  CONSTRAINT `fk_Books_has_Category_Books1`
    FOREIGN KEY (`Books_ISBN`)
    REFERENCES `database`.`Books` (`ISBN`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Books_has_Category_Category1`
    FOREIGN KEY (`Category_Name`)
    REFERENCES `database`.`Category` (`Name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Authored`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Authored` (
  `Authors_AuthorID` INT NOT NULL,
  `Books_ISBN` VARCHAR(18) NOT NULL,
  PRIMARY KEY (`Authors_AuthorID`, `Books_ISBN`),
  INDEX `fk_Authors_has_Books_Books1_idx` (`Books_ISBN` ASC),
  INDEX `fk_Authors_has_Books_Συγγραφεί_idx` (`Authors_AuthorID` ASC),
  CONSTRAINT `fk_Authors_has_Books_Authors1`
    FOREIGN KEY (`Authors_AuthorID`)
    REFERENCES `database`.`Authors` (`AuthorID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Authors_has_Books_Books1`
    FOREIGN KEY (`Books_ISBN`)
    REFERENCES `database`.`Books` (`ISBN`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `database`.`Reminds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `database`.`Reminds` (
  `Staff_StaffID` INT NOT NULL,
  `Members_MemberID` INT NOT NULL,
  `Date of Reminder` DATE NULL,
  PRIMARY KEY (`Staff_StaffID`, `Members_MemberID`),
  INDEX `fk_Staff_has_Members_Members1_idx` (`Members_MemberID` ASC),
  INDEX `fk_Staff_has_Members_Worker_idx` (`Staff_StaffID` ASC),
  CONSTRAINT `fk_Staff_has_Members_Staff1`
    FOREIGN KEY (`Staff_StaffID`)
    REFERENCES `database`.`Staff` (`StaffID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Staff_has_Members_Members1`
    FOREIGN KEY (`Members_MemberID`)
    REFERENCES `database`.`Members` (`MemberID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -- -----------------------------------------------------
-- -- Table `database`.`Books`
-- -- -----------------------------------------------------
-- CREATE TABLE IF NOT EXISTS `database`.`Books` (
--   `ISBN` VARCHAR(18) NOT NULL,
--   `Title` VARCHAR(80) NULL,
--   `Pages` INT NULL,
--   `Publication_Year` INT NULL,
--   `Publishers_Name` VARCHAR(60) NOT NULL,
--   `LibraryName` VARCHAR(10) NOT NULL,
--   `Author` VARCHAR(80) NOT NULL,
--   PRIMARY KEY (`ISBN`),
--   INDEX `fk_Books_Publishers1_idx` (`Publishers_Name` ASC),
--   CONSTRAINT `fk_Books_Publishers1`
--     FOREIGN KEY (`Publishers_Name`)
--     REFERENCES `database`.`Publishers` (`Name`)
--     ON DELETE CASCADE
--     ON UPDATE CASCADE,
--   CONSTRAINT `fk_Books_Library1`
--     FOREIGN KEY (`LibraryName`)
--     REFERENCES `database`.`Library` (`LibraryName`)
--     ON DELETE CASCADE
--     ON UPDATE CASCADE)
-- ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
