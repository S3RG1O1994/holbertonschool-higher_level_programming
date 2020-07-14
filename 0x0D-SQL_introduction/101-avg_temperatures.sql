-- New task
SELECT city,AVG(values) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;