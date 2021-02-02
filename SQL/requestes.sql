--1
select contactLastName, contactLastName,country,state, city from customers group by country,state, city;
--2
select count(*) from employees;
--3 
select SUM(quantityOrdered*priceEach ) AS prix_total from orderdetails; -- 9604190.61
--4
select * from products where productLine ='Classic Cars' or productLine = 'Vintage Cars';
--5 
select sum(amount) from payments where paymentDate = '2004-10-28';
--6 
select *  from payments where amount > 100000;
--7 
select distinct productName from products;
--8
select sum(productName), productLine from products group by productLine ;
--9
select min(amount) from payments;
--10
SELECT amount FROM payments having amount > (AVG(amount)*2);
--11

