# Joins

# Inner Join

select employees.first_name, employees.last_name, employees.email, projects.project_name, projects.department
from employees
inner join projects on projects.employee_id = employees.employee_id;


# Left join

select employees.first_name, employees.last_name, employees.email, projects.project_name, projects.department
from employees
left join projects on projects.employee_id = employees.employee_id;


# Right Join

select employees.first_name, employees.last_name, employees.email, projects.project_name, projects.department
from employees
right join projects on projects.employee_id = employees.employee_id;


# Full Join

select employees.first_name, employees.last_name, employees.email, projects.project_name, projects.department
from employees
full join projects on projects.employee_id = employees.employee_id;
