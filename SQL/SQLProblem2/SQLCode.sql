CREATE TABLE STUDENTS(
	STUDENTNUMBER INT PRIMARY KEY NOT NULL,
	STUDENTNAME CHAR(50) NOT NULL,
	STUDENTAGE INT NOT NULL
)


INSERT INTO STUDENTS VALUES
(1,"Nils-Erik", 21),
(2,"Olav", 22),
(3,"Zorab", 22),
(4,"Marcus", 23)

SELECT * FROM STUDENTS WHERE STUDENTAGE>21