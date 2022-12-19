# Aggregation 


# MAX

select max(maths) from school;
select max(maths) as max_m from school;

# MIM

select min(maths) from school;
select min(maths) as min_m from school;

# COUNT

select count(*) from school;

# SUM

select sum(english) from school;

# CASE

SELECT name,maths,english,
CASE
WHEN grade=’S’ THEN ‘pass’
end as resu
from school;


# NULL

select * from school where grade is NULL;

# Date Function

select now();
select curtime();
select adddate(‘2020–01–02’, 31);
SELECT DATE_ADD(‘2021–01–02’, INTERVAL 31 DAY);
select curdate();
SELECT DATEDIFF(‘2007–12–31 23:59:59’,’2007–12–30');
SELECT DAYNAME(‘1992–05–18’);








	