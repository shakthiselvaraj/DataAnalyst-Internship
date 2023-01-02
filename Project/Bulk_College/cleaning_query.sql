SELECT * FROM bulk_college.details;

# Cleaning Column College_Name

alter table details rename column collegename to College_Name;

select College_Name from details order by College_Name;

select count(College_Name) from details
where College_Name is null;

select College_Name, COUNT(College_Name)
from details
group by  College_Name
having count(College_Name) > 1;

select * from details
where College_Name = 'NATIONAL INSTITUTE OF FASHION TECHNOLOGY';

select * from details
where College_Name ='Institute of Hotel Management, Catering Technoloty & Applied Nutrition';

update details
set College_Name = upper(College_Name);

# Cleaning Column State

alter table details rename column state to State;

select State from details;

select count(State) from details
where State is null;

select State, COUNT(State)
from details
group by  State
having count(State) > 0;

select concat(upper(substr(State,1,1)),lower(substr(State,2))) as States from details;

update details set State = concat(upper(substr(State,1,1)),lower(substr(State,2)));


# Cleaning Column District

alter table details rename column district to District;

select District from details;

select count(District) from details
where District is null;

select District, COUNT(District)
from details
group by  District
having count(District) > 0;

select concat(upper(substr(District,1,1)),lower(substr(District,2))) as Districts from details;

update details set District = concat(upper(substr(District,1,1)),lower(substr(District,2)));

# Cleaning Column E-Mail

alter table details rename column mail to E_Mail;

select E_Mail from details;

select count(E_Mail) from details
where E_Mail is null;

select E_Mail, COUNT(E_Mail)
from details
group by  E_Mail
having count(E_Mail) > 1;

select count(E_Mail) from details
where E_Mail not regexp "^[a-zA-Z0-9][a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$";

update details
set E_Mail = 'Unavailable'
where E_Mail not regexp "^[a-zA-Z0-9][a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$";

select E_Mail from details
where  E_Mail  regexp "^[a-zA-Z0-9][a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$";

# Cleaning Column Phone_No

alter table details rename column phone to Phone_No;

select Phone_No from details;

select Phone_No from details
where Phone_No is null;

update details set Phone_No = 'Unavailable'
where Phone_No is null;

select  Phone_No from details where not  regexp_like(Phone_No,'(0|91)?[6-9][0-9]{9}');

update details set Phone_No = 'Unavailable'
where not  regexp_like(Phone_No,'(0|91)?[6-9][0-9]{9}');


select id from details;
alter table details rename column id to Serial_No;

select  row_number() over(order by College_Name) as ID from details;







