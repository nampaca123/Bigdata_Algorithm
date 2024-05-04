--select SUM(saleprice) AS 총매출
--From Orders;
--For using meaningful column name, 'AS' is needed to give it a nickname

---select SUM(saleprice) AS 총매출
---From Orders 
---where custid=2;

SELECT SUM(saleprice) AS TOTAL,
AVG(saleprice) AS Average,
COUNT(saleprice) AS COUNT,
MIN(saleprice) AS Minimum,
MAX(saleprice) AS Maximum
From Orders; 