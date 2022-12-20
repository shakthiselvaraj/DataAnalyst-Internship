# Temporary Table

# Local

create table #company(name char(20), project char(30), salary int);

insert into #company(name,project,salary) values ('aiai', 'python', 40000);



# Global

create table ##company(name char(20), project char(30), salary int);

insert into ##company(name,project,salary) values ('aiai', 'python', 40000);


