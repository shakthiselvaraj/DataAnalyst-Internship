SELECT * FROM amazon.final_book_dataset_kaggle;
alter table  amazon.final_book_dataset_kaggle rename to books;

select * from books;
desc books;
 
 
  
# Which book (title) recieved max reviews
select * from books
where n_reviews = (select max(n_reviews) from books);

# Which book has most percentage of 5 stars?
select * from books
where star5 = (select max(star5) from books);


# Which publisher is most famous?
select author, publisher from books
where n_reviews = (select max(n_reviews) from books);

# Which language is most preffered by readers?
select language, count(language) as counts from books
group by language;

# What are the average number of pages
select avg(pages) from books;