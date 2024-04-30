create table Newbook (
    bookid number,
    bookname varchar2(20) not NULL,
    publisher varchar2(20) UNIQUE,
    price NUMBER default 10000 check(price > 1000),
    primary key(bookid)
);

-- Bookname is not null, publisher is not same value, price is 10000 as a default if price is not interpreted, price is at least 1000
