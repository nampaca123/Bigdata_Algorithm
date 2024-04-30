select orderid, saleprice from Orders
where saleprice > ALL (select saleprice from orders where custid='3');

--Can use ALL, SOME, ANY right after >, <, <=, ! ...