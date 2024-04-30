select name from customer 
MINUS
select name from customer
where custid IN (select custid from orders)
--IN Oracle = Minus, IN Standard SQL = Except
