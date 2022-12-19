# To Create Table

create table school(name char(30),section char(10),english int,maths int,grade char(30));

# Alter Taable

alter table school add tamil int;
alter table school add(science int, social int);
alter table school rename column section to sec;
alter table school modify name char(35);

# Insert Table

insert into school (name,sec,english,maths,tamil,science,social,grade) values ('aiai','B',85,75,68,95,55,'B');
insert into school (name,sec,english,maths,tamil,science,social,grade) values ('bibi','C',95,66,87,65,87,'B');
insert into school (name,sec,english,maths,tamil,science,social,grade) values ('cici','A',85,66,75,66,65,'A');
insert into school (name,sec,english,maths,tamil,science,social,grade) values ('didi','B',99,88,99,86,97,'S');
insert into school (name,sec,english,maths,tamil,science,social,grade) values ('eiei','C',85,65,77,84,65,'C');
insert into school (name,sec,english,maths,tamil,science,social,grade) values ('fifi','A',95,86,87,95,87,'A');

# Update Table

update school set maths = 90 where name = 'bibi';

# Select Table

select * from school;
select maths from school;
select english from school where name = 'aiai';

# Select using AND OR NOT LIKE

select maths , english from school where grade ='A' and sec = 'A';
select name from school where grade ='A' or sec ='B';
select * from school where not grade ='A';
select * from school where maths like 66;




