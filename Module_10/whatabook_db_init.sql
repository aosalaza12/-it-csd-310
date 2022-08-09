
/*

whatabook_db_init.sql
Author: Alvaro Salazar
Date: March 4, 2022

*/
-- Delete and Create a new MySQL database and name it whatabook
DROP SCHEMA IF EXISTS whatabook;
 
CREATE DATABASE whatabook;

USE whatabook;

-- drop user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create a new database user and name it whatabook_user and assign it the password MySQL8IsGreat! 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- drop contstraints if exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- Create table(s) for whatabook Data Base

-- store: Do not set the store_id field to auto increment, because when the business expands, each business could assign its own store ID codes. 

CREATE TABLE store (
    store_id    INT             NOT NULL,
    locale      VARCHAR(500)    NOT NULL,
    hour_open   TIME            NOT NULL,
    hour_closed TIME            NOT NULL,
    PRIMARY KEY(store_id)
);

-- book
CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    store_id    INT             NOT NULL,
    PRIMARY KEY(book_id)
);

-- user
CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

-- wishlist
CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


-- Insert new records to fill each table

-- Store table

INSERT INTO store(store_id, locale, hour_open, hour_closed)
    VALUES(1, '2454 Parsons Pond, Kissimmee, FL, 34743', '08:00:00', '20:00:00');


-- book table

INSERT INTO book(book_name, details, author, store_id)
    VALUES('Clean Code', 'The authors are highly experienced craftsmen and professionals about Code' ,'Robert C. Martin', 1),
          ('SQL Injection Attacks and Defense', 'Knowledge and best practice in this field are constantly changing', 'Justin Clarke', 1),
          ('SQL Server', 'is based on my Sams Teach Yourself SQL in 10 Minutes', 'Ben Forta', 1),
          ('NoSQL', 'A Brief Guide to the Emerging World of Polyglot Persistence', 'Pramod J. Sadalage, Martin Fowler', 1),
          ('Network Defense and Countermeasures', 'Excelent', 'Chuck Easttom', 1),
          ('IT Audting', 'Using controls to protect Information Assets', 'Mike Kegerreis, Mike Schiller, Chris Davis', 1),
          ('Access Control and Identity Management', 'Access control goes beyond the simple username and password', 'Mike Chapple', 1),
          ('Fundamentals of Information Systems Security', 'May your passion for learning IT Security help you protect the information', 'David Kim, Michael G. Solomon', 1),
          ('How to create your own apps business', 'Naking money by selling your apps', 'George Lucas', 1);

-- user table

INSERT INTO user(first_name, last_name)
    VALUES('Alvaro', 'Salazar'),
          ('George', 'Washington'),
          ('Thomas', 'Jefferson');

-- wishlist table 

INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 1),
          (2, 6),
          (3, 8);

--
