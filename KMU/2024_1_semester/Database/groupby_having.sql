--select custid, COUNT(*) AS 도서수량, SUM(saleprice) AS 총액
--from Orders 
--Group by custid;

select custid, COUNT(*) AS 도서수량
From Orders Where saleprice >= 8000
Group by custid having count(*) >=2
--Search customer who only ordered more than 2 books