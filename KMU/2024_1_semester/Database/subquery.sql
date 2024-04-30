select name from CUSTOMER
where custid IN (select custid from orders
where bookid IN (select bookid from BOOK
where publisher = '대한미디어'));
--Show the customer's name who bought book published from '대한미디어'