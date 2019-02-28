CREATE view article_view_number AS
SELECT title, author, COUNT(*) AS views
FROM articles, log
WHERE log.path LIKE CONCAT('%', articles.slug)
GROUP BY articles.title, articles.author
ORDER BY views DESC;



CREATE view error_log AS 
SELECT date(log.time), ROUND(100.0*SUM(case log.status WHEN '200 OK' then 0 else 1 END)/COUNT(log.status), 2) AS Percent_Error
FROM log
GROUP BY date(log.time)
ORDER BY Percent_Error DESC;  