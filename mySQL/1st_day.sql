use 1st_day_on_SQL;

use Tables;

select * from students;

select count(region) from students;

select count(*) as total_no_of_records from students;

select region from students;

select  count(distinct(age)) from students; # DISTINCT -> it removes dublicates to return only unique values
select * from students limit 5;

select * from students su;

select * from students;

select age_cate, stay_cate, japanese_cate
from students
limit 5;

select region,academic,age from Students
# where toas>20;
where gender = "Male";

select * from Students
where age = 24 or japanese_cate = "Average";

select count(*) from Students
where age = 24 or japanese_cate = "Average";

select * from Students
where age = 24 and japanese_cate = "Average";

select * from Students
where age 
between 24 and 34 ;

select * from Students 
where age 
between 24 and 34 and gender = "Female";

select academic,stay,stay_cate,age from students
where stay like '1%';

select academic,stay,stay_cate,age from students
where academic like 'U%';

select academic,stay,stay_cate,age from students
where academic like '%d'; # In academic those words ends with 'd' the all are show in o/p.

select academic,stay,stay_cate,age from students
where academic like '__d%';  # only 3rd position word 'd' will be shown in o/p.

select * from students
where stay_cate in ("Long","Short");

# Aggregate Function

select avg(age) as age from students;

select sum(age) as age from students;

select min(age) as age from students;

select max(age) as age from students;

select count(age) as age from students;

#Using WHERE with Aggregate Function

select sum(age) as age from students
where gender='Male';

# ROUND() -> Round a number to a specified decimal
 
select round(sum(age)) as age from students
where gender='Male';

select round(sum(age),2) as age from students # 2 -> it only show 2 number after decimal
where gender='Male';

select * from students;
select age, gender from students order by gender desc; # desc -> descending order of gender

select * from students;
select age, gender from students order by gender ;

select * from students;
select age, gender from students order by age asc; # asc -> ascending order of age 

select stay_cate, round(sum(age)) as total_sum
from students
group by stay_cate
order by total_sum desc;