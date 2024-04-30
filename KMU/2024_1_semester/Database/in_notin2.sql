select sum(saleprice) "total"
from Orders
Where custid IN (select custid from Customer Where address LIKE '%대한민국%');