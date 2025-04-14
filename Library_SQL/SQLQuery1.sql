/*

Library Mangement
Zahra Sedaghat				990122681003
Farid Afrakhte				990122680092

*/


-- Creating Our DB
CREATE DATABASE LibraryManagement;					
USE LibraryManagement;							    	

--	Delete table if exists
DROP TABLE if EXISTS Book;

--	Create 'Book' table
CREATE TABLE Book (

--	Adding Columns to the 'Book' table 
Title VARCHAR(20) ,
ISBN INT PRIMARY KEY,
Edition INT,
Genre VARCHAR(20),
Available BIT,
Publisher VARCHAR(20),
Author VARCHAR(20)
);

--	Adding Records to the 'Book' table
INSERT INTO Book (Title, ISBN, Edition, Genre, Available, Publisher, Author)
VALUES
   ('TooLate',     74390, 4, 'Love',              1, 'Macmillan', 'ColleenHoover'),
   ('Layla',       92467, 2, 'Horror',            0, 'Macmillan', 'ColleenHoover'),
   ('UglyLove',    08241, 2, 'Fantasy',           1, 'Pearson',   'ColleenHoover'),
   ('Verity',      64306, 1, 'Fable',             1, 'Pearson',   'ColleenHoover'),
   ('OneMoreStep', 43597, 3, 'HistoricalFiction', 0, 'Macmillan', 'ColleenHoover')
   ;

   
--	Delete table if exists
DROP TABLE if EXISTS Member;

--	Create 'Member' table
CREATE TABLE Member (

--	Adding Columns to the 'Member' table 
M_Name VARCHAR(20) ,
M_IDNO INT PRIMARY KEY ,
MembershipDate DATE ,
M_Email VARCHAR(50),
M_PhoneNumber VARCHAR(12),
M_Pass VARCHAR(10) NOT NULL Default 'PASS'

);

--	Adding Records to the 'Member' table
INSERT INTO Member (M_Name, M_IDNO, MembershipDate, M_Email, M_PhoneNumber)
VALUES
	('Farid',    78964812, '2023-12-16', 'farid1231@tsderp.com', '09919017654'),
	('Masoumeh', 98712547, '2026-11-17', 'kefowo5427@email.com', '09126643987'),
	('Alireza',  66988741, '2027-06-19', 'ali7654@yahoo.com',    '09132654397'),
	('Amin',     74825413, '2021-01-05', 'amin986@gmail.com',    '09117631298'),
	('Sanaz',    85214736, '2025-05-03', 'sanaziii87.yahoo.com', '09198711889'),
	('Zahra',    78935491, '2024-09-04', 'zahraaaa986@mail.com', '09871235609')
   ;


--	Delete table if exists
DROP TABLE if EXISTS Staff;

--	Create 'Staff' table
CREATE TABLE Staff (

--	Adding Columns to the 'Staff' table 
S_Name VARCHAR(10) ,
S_IDNO INT PRIMARY KEY ,
Contract DATE , 
S_Pass VARCHAR(10) NOT NULL Default 'PASS'
);

--	Adding Records to the 'Staff' table
INSERT INTO Staff (S_Name, S_IDNO, Contract)
VALUES
   ('Ali',      85408632, '2025-08-17'),
   ('Mohammad', 87963249, '2029-07-15'),
   ('Zahra',    54982173, '2025-03-06'),
   ('Fatemeh',  87594217, '2027-11-18'),
   ('Hossein',  95874366, '2022-10-04')
   ;


--	Delete table if exists
DROP TABLE if EXISTS Borrow;

--	Create 'Borrow' table
CREATE TABLE Borrow (

--	Adding Columns to the 'Borrow' table 
M_IDNO INT FOREIGN KEY REFERENCES dbo.MEMBER(M_IDNO),
ISBN INT FOREIGN KEY REFERENCES dbo.Book(ISBN) ,
BorrowDate DATE NOt NULL Default '2024-01-24',
DueDate DATE NOt NULL Default '2024-02-24'

);

--	Adding Records to the 'Borrow' table
INSERT INTO Borrow (M_IDNO, ISBN, BorrowDate, DueDate)
VALUES
	(78964812, 43597, '2024-02-17', '2024-03-17'),
	(98712547, 92467, '2024-02-15', '2024-03-15')
	;

SELECT * FROM BOOK;
SELECT * FROM Staff;
SELECT * FROM Member;
SELECT * FROM Borrow;
