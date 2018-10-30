CREATE TABLE Suppliers(
	SupplierID INT NOT NULL,
	CompanyName CHAR(50) NOT NULL,
	StreetAddress CHAR(50) NOT NULL,
	City CHAR(50) NOT NULL,
	COUNTRY CHAR(50) NOT NULL,
	PHONE INT NOT NULL,
	PRIMARY KEY(SupplierID)
)

INSERT INTO Suppliers VALUES(1, "SupplierA", "Hatlevien", "Bergen", "Norway", 92121221),
(2, "SupplierB", "Oyamazaki", "kyoto", "Japan", 93521221),
(3, "SupplierC", "Herlev", "Copenhagen", "Denmark", 94521221),
(4, "SupplierD", "Regeringsgatan 65", "Stockholm", "Sweden", 95521221),
(5, "SupplierE", "Tianhe N Rd", "Guangzhou", "China", 96121221)








