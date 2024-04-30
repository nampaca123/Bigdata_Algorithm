select custid, (select name from  Customer cs Where cs.custid=od.custid), SUM(SALEPRICE)
from Orders od
Group by custid

--Scalar Subquery can be putted to nearly everywhere, but especially to SELECT and UPDATE SET