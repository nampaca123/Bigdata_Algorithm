create table NewOrders2 (
    orderid Number,
    custid Number Not Null,
    bookid Number Not Null,
    Saleprice Number,
    Orderdate Date,
    Primary Key(orderid),
    Foreign Key (custid) References NewCustomer(custid) on Delete Cascade
);