Create or replace VIEW vw_Orders (Orderid, custid, name, bookid, bookname, saleprice, orderdate)
As select od.orderid, od.custid, cs.name, od.bookid, bk.bookname, od.saleprice, od.orderdate
From Orders od, Customer cs, Book bk
Where od.custid=cs.custid AND od.bookid = bk.bookid;

Select orderid, bookname, SALEPRICE
From vw_Orders
Where name = '김연아';