drop table Summer;

create table Summer(
    sid Number,
    class Varchar2(20),
    price number
);

insert into Summer values (100, 'Fortain', 20000);
insert into Summer values (150, 'Pascal', 15000);
insert into Summer values (200, 'C', 10000);
insert into Summer Values (250, 'Fortain', 20000);

select * from Summer;