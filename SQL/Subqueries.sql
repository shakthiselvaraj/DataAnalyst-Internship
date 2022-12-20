# Subqueries


# scaler
# Employe who earns more than the average salary of all employee

select * from employees
where salary >(select avg(salary) from employees);




# Multiple row
# Employee Who earn the maximum salary of all employee in several departments

select * from employe
where salary in (select  max(salary) from employees group by deptid);




# Corelated 
# Employee Who earns more than the average salary of all employee in that  department

select * from employe e1
where salary > (select avg(salary) from employe e2 where e2.deptid = e1.deptid);
