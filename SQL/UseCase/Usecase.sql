# Use Case Implementation

#  What is the number of registered users by country?

select country_code, count(*) as resgistered_user
from users
group by country_code;



# What is the percentage of users who made their first payment 3 days after registration by country?

select users.country_code,
count(distinct users.user_id) registered,
count(distinct a.user_id) first3dayspayment,
(cast(count(distinct a.user_id) as real)  / count(distinct  users.user_id)) * 100  percentage
from users 
left join 
(select payments.user_id, payments.created_at, users.joined_at,
rank() over(partition by user_id order by (created_at)) ranks
from payments 
join users on users.user_id = payments.user_id
where (payments.created_at) >= (users.joined_at)) a
on users.user_id = a.user_id and a.created_at - a.joined_at  <= 3 and ranks = 1
group by 
users.country_code;

# What is the percentage of users who made more than 1 executed booking?

select count(users.user_id) registered,
count(a.user_id) executed,
round(cast(count(a.user_id) as real) / count(users.user_id) * 100, 1) percentage
from users
left join
(select user_id, count(id) Executed from bookings
where status ="Executed"
group by user_id
having Executed >1)a
on a.user_id = users.user_id;

# What is the Weekly Cancellation Rate?

select week(a.starttime) weekly,
count(a.id) counts,
count(b.id) cancel,
round((cast(count(b.id) as real) / count(a.id)) * 100, 1) cancelrate
from bookings a
left join 
bookings b on b.id = a.id and b.status = "Cancelled"
group by
weekly;


#  Describe booking Behaviour per year (any trends?).

select status, count(status) as counts,
date_format(Starttime,'%y') AS Years
from bookings
group by status,years;
    
    