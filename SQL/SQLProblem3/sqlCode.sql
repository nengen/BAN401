CREATE TABLE OUTLETS(
	OUTLET_ID INT PRIMARY KEY NOT NULL,
	OUTLET_NAME CHAR(50) NOT NULL,
	ORGANIZATIONAL_NUMBER INT NOT NULL,
	ADRESS CHAR(50) NOT NULL,
	CITY CHAR(50) NOT NULL,
	ZIP_CODE INT NOT NULL
)
INSERT INTO OUTLETS VALUES
(1,"Oscars", 101054687, "King Oscars", "Bergen", 5018),
(2,"Beck", 548675839, "Jebsen Street", "Oslo", 3030)


CREATE TABLE OUTLET_KEY_FIGURES(
	OUTLET_ID INT PRIMARY KEY NOT NULL,
	SALES INT NOT NULL,
	COSTS INT NOT NULL,
	FOREIGN KEY (OUTLET_ID) REFERENCES OUTLETS (OUTLET_ID)
)

INSERT INTO OUTLET_KEY_FIGURES VALUES
(1,10000, 6000),
(2,20000,10000)

CREATE TABLE PRODUCTS(
	PRODUCT_ID INT NOT NULL,
	OUTLET_ID ID NOT NULL,
	PRODUCT_CATEGORY INT PRIMARY KEY NOT NULL,
	PRODUCT_NAME CHAR(50) NOT NULL,
	PRODUCT_STOCK INT NOT NULL,
	PRODUCT PRICE INT NOT NULL,
	FOREIGN KEY (OUTLET_ID) REFERENCES OUTLETS (OUTLET_ID)
)
INSERT INTO PRODUCTS VALUES
(1,1, "A", "Ivory", 0, 10000),
(2,1, "B", "Green Beans", 10000, 0.99)

