select orderid "Order Number", To_CHAR(orderdate, 'yyyy-mm-dd dy') "Order Day", custid "Customer ID", bookid "BOOK ID"
from Orders
where orderdate=TO_DATE('20200707','yyyymmdd')