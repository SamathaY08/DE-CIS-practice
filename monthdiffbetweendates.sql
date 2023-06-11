create table Sales
(
customerid int,
dateno varchar(20),
)

insert into sales values(1111,'202212'),(1111,'202210'),(1111,'202209'),(1111,'202301'),(2222,'202201'),(2222,'202205'),(2222,'202204')


select s.customerid,s.dateno,(((round((s.dateno/100),0)-round((min(s1.dateno)/100),0))*12)+(s.dateno%100-min(s1.dateno)%100)) as monthsdifference
from sales as s
join sales as s1 on s.customerid=s1.customerid
group by s.customerid,s.dateno



create table sales1
(
customerid int,
dateno date,
)

insert into sales1 values(1111,'2022-12-1'),(1111,'2022-10-1'),(1111,'2022-09-1'),(1111,'2023-01-1'),(2222,'2022-01-01'),(2222,'2022-05-02'),(2222,'2022-04-01')
select * from sales1

with cte1 (customerid,dateno,startdate) as
(
select customerid, dateno,
 min(dateno) OVER (PARTITION by customerid) as startdate
from sales1
)
select customerid,dateno,abs(Datediff(month,dateno,startdate)) as difference
from cte1







