-- New task
SELECT city, AVG(values) AS avg_temp FROM hbtn_0c_0 GROUP BY city ORDER BY avg_temp DESC;