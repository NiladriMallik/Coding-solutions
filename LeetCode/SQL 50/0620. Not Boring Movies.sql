# Write your MySQL query statement below
SELECT * FROM CINEMA
WHERE ID % 2 != 0 AND DESCRIPTION NOT IN ("boring")
ORDER BY RATING DESC
;