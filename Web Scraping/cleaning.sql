SELECT * FROM ptu_colleges.details;
update details
set College_Names = substring_index(College_Names,',',1) ;
update details
set Phone_No = substr(Phone_No, 1, 10); 

update details set Phone_No = 'Unavailable'
where not  regexp_like(Phone_No,'(0|91)?[6-9][0-9]{9}');




