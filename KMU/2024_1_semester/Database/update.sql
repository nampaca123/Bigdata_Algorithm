update CUSTOMER
set address = (select address from customer where name = '김연아')
where name like '박세리';