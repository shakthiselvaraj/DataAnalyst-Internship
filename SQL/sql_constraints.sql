# SQL constraints

# Primary,Not Null,Unique

create table branch(branch_id int primary key, location char(20) unique, address char(30) not null);

alter table branch modify address varchar(20); 

insert into branch (branch_id, location, address) values (1, 'chennai', '10,aiai road');

insert into branch (branch_id, location, address) values (2, 'salem', '11,bibi road'),
                                                         (3, 'mumbai', '12,abc road'),
                                                         (4, 'banglore', '113,bh road'),
                                                         (5, 'goa', '15,fro road'),
                                                         (6, 'pune', '1,fg road');
                                                         
select * from branch;


# Foreign Key

create table employees(id int not null primary key, name char(20), position char(20), salary int, branch_id int, foreign key(branch_id) references branch(branch_id));

insert into employees(id, name, position, salary, branch_id)
values
(1, 'aiai', 'admin',15000,2),
(2, 'bibi', 'hr',500000,4),
(3, 'cici', 'manager',400000,2),
(4, 'didi', 'sales',250000,3),
(5, 'eiei', 'clerk',10000,6),
(6, 'fifi', 'suppoter',120000,1),
(7, 'gigi', 'hr',650000,1),
(8, 'hihi', 'manager',55500,5),
(9, 'iiii', 'admin',15000,4),
(10, 'jiji', 'sales',250000,3);

select * from employees;


# Check

create table finance(amount int check (amount>=1500));

insert into finance (amount) values (1500),(4000),(30000);   #valid
insert into finance (amount) values (200),(400),(30000);     #not valid

# Default

create table college (college_id int primary key,college_code varchar(20),college_country varchar(20) default ('India');

# Create Index

create table branch(branch_id int primary key, location char(20) not null,address char(30));

create index branch_index on branch(location);

