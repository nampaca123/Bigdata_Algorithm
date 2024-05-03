
 DROP TABLE SummerPrice;
 DROP TABLE SummerEnroll;

 CREATE TABLE SummerPrice
 (   
class VARCHAR2(20),
 price NUMBER
 );
 INSERT INTO SummerPrice VALUES ('FORTRAN', 20000);
 INSERT INTO SummerPrice VALUES ('PASCAL', 15000);
 INSERT INTO SummerPrice VALUES ('C', 10000);
 SELECT * FROM SummerPrice;

 CREATE TABLE SummerEnroll
 (   
sid NUMBER,
 class VARCHAR2(20)
 );
 INSERT INTO SummerEnroll VALUES (100, 'FORTRAN');
 INSERT INTO SummerEnroll VALUES (150, 'PASCAL');
 INSERT INTO SummerEnroll VALUES (200, 'C');
 INSERT INTO SummerEnroll VALUES (250, 'FORTRAN');
 SELECT * FROM SummerEnroll;