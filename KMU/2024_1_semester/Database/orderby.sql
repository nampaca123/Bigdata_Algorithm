--select * from Book order by price, bookname
--if price is same, bookname will be the order
select * from Book order by price DESC, publisher ASC;
-- DESC price as first, if price is ==, publisher will be secondery order!