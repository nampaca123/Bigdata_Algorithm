--select name, sum(saleprice) 
--from customer, orders
--where customer.custid = orders.custid
--group by customer.name
--order by CUSTOMER.name;

--select Customer.name, Book.BOOKNAME
--From Customer, Orders, Book
--Where Customer.custid = Orders.custid And Orders.bookid = Book.bookid
--And Book.price = 20000;
-- Find out the customer's name who ordered book which price is 20,000 and its bookname

--Outer Join
Select Customer.name, Orders.SALEPRICE
From Customer Left outer join ORDERS
On CUSTOMER.CUSTID = Orders.CUSTID;