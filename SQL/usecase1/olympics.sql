SELECT * FROM usecase2.athlete_events;

alter table usecase2.athlete_events rename to events;

select * from events;

SELECT * FROM usecase2.noc_regions;

alter table usecase2.noc_regions rename to regions;

select * from regions;

# 1. How many olympics games have been held?

select  count(distinct games) total_games from events; 

# 2. List down all Olympics games held so far.
select distinct year,season,city,games from events order by year;

# 3. list down all NOC
select count(distinct NOC) total_no_nations from events;

# 4. Mention the total no of nations who participated in each olympics game?
with a as(select games, region from events join regions ON regions.noc = events.noc
group by games, regions.region) 
(select games, count(1) as total_countries from a group by games
order by games);

# 5. Identify the sport which was played in all summer olympics.
select count(distinct games) as total_games from events where season = 'Summer';
select distinct games, sport from events where season = 'Summer' order by games;

