select cs.name, SUM(od.saleprice) "total"
From (select custid, name from Customer Where custid <= 2) cs, Orders od
where cs.custid=od.custid 
Group by cs.name;

--Inline view can be used in From sector, like normal tables
--But as it is view form, cannot be used as relational subquery