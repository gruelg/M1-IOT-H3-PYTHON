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
select amount from payments where amount > (select avg((amount*2)) from payments);
--11
select test from products having test = AVG(buyPrice-MSRP); -- faut a refaire 
--12
select distinct count(productName) from products;
--13
select customerName, city from customers where salesRepEmployeeNumber is NULL;
--14 
select CONCAT(lastName," ", firstName) from employees where jobTitle like 'VP%' or jobTitle like '%Manager%';
--15
select orderNumber, SUM(quantityOrdered*priceEach ) AS prix_total from orderdetails having prix_total > 5000;
--16
select CONCAT(customers.contactLastName," ", customers.contactLastName) as customer ,CONCAT(employees.lastName," ", employees.firstName) as employees from customers, employees where customers.salesRepEmployeeNumber = employees.employeeNumber;	
--17
select SUM(amount ) AS prix_total from payments where customerNumber = ( select customerNumber from customers where customerName = 'Atelier graphique');
--18
select sum(amount), paymentDate from payments group by paymentDate;
--19
select productName from products where productCode not in ( select productCode from orderdetails);
--20
select CONCAT(customers.contactLastName," ", customers.contactLastName) as customer, sum(payments.amount) as payment from customers, payments where customers.customerNumber = payments.customerNumber group by payments.customerNumber;
--21
select count(status) from orders where status ='On Hold';
--22
SELECT orderNumber FROM orders where DAYOFWEEK(orderDate) = 2;
--23
select products.productName from customers, orders, orderdetails, products where customers.customerNumber = orders.customerNumber and orders.orderNumber = orderdetails.orderNumber and orderdetails.productCode = products.productCode and  customers.customerName = 'Herkku Gifts';
--24
select * from orderdetails group by orderNumber, productCode limit 5;
