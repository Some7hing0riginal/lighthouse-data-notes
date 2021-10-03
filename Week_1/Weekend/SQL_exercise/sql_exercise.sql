/* SQL Exercise
====================================================================
We will be working with database imdb.db
You can download it here: https://drive.google.com/file/d/1E3KQDdGJs4a0i1RoYb8DEq0PFxCgI6cN/view?usp=sharing
*/


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE
SELECT * FROM movies;

SELECT * FROM movie_distributors;

SELECT * FROM distributors;
--==================================================================
/* TASK I
 Find the id's of movies that have been distributed by “Universal Pictures”.
*/
SELECT movies.movie_id
FROM movies
JOIN movie_distributors ON movie_distributors.movie_id = movies.movie_id
JOIN distributors ON distributors.distributor_id = movie_distributors.distributor_id
WHERE distributors.name = "Universal Pictures";
/* TASK II
 Find the name of the companies that distributed movies released in 2006.
*/
SELECT distributors.name
FROM movies
JOIN movie_distributors ON movie_distributors.movie_id = movies.movie_id
JOIN distributors ON distributors.distributor_id = movie_distributors.distributor_id
WHERE movies.year = 2006;


/* TASK III
Find all pairs of movie titles released in the same year, after 2010.
hint: use self join on table movies.
*/
SELECT * FROM movies a
JOIN movies b ON a.year = b.year
WHERE a.year > 2010;

/* TASK IV
 Find the names and movie titles of directors that also acted in their movies.
*/
SELECT *
FROM movies
JOIN directors USING(movie_id)
JOIN people ON directors.person_id = people.person_id
JOIN roles ON roles.person_id = directors.person_id;

/* TASK V
Find ALL movies realeased in 2011 and their aka titles.
hint: left join
*/
SELECT movies.title, aka_titles.title FROM movies
LEFT JOIN aka_titles USING(movie_id);



/* TASK VI
Find ALL movies realeased in 1976 OR 1977 and their composer's name.
*/
SELECT movies.title FROM movies
WHERE movies.year = 1976 OR movies.year = 1977;



/* TASK VII
Find the most popular movie genres.
*/
SELECT movies.title, genres.label FROM movies
JOIN movie_genres USING(movie_id)
JOIN genres USING(genre_id);

SELECT genre_id, label, COUNT(genre_id) as count FROM movie_genres
JOIN genres USING (genre_id)
GROUP BY genre_id
ORDER BY count DESC;

/* TASK VIII
Find the people that achieved the 10 highest average ratings for the movies 
they cinematographed.
*/



/* TASK IX
Find all countries which have produced at least one movie with a rating higher than
8.5.
hint: subquery
*/




/* TASK X
Find the highest-rated movie, and report its title, year, rating, and country. There
can be ties; if so, you should report for each of them.
*/




/* STRETCH BONUS
Find the pairs of people that have directed at least 5 movies and whose 
carees do not overlap (i.e. The release year of a director's last movie is 
lower than the release year of another director's first movie).
*/
