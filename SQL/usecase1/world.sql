SELECT * FROM world.city;


select  count(countrycode) from city;

# list out the maximum population
select distinct * from city
where Population=(select max(population) from city);

# list out no.of district in country
select countrycode,count(district) from city group by countrycode; 

# List out totlal No.of population in each country
select countrycode,sum(population) populations from city group by countrycode;


# list out no.of language in country
select countrycode,count(language) from countrylanguage group by countrycode; 

# lit out total percentage of each country
select countrycode,sum(percentage) percentages from countrylanguage group by countrycode; 