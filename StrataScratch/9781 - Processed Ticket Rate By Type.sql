-- My Solution = 0.02455 seconds
WITH CTE1 AS(
    SELECT
        TYPE,
        CAST(COUNT(TYPE) AS FLOAT) AS PROCESSED_COUNTS
    FROM FACEBOOK_COMPLAINTS
    WHERE PROCESSED = 'TRUE'
    GROUP BY TYPE
),
CTE2 AS(
    SELECT
        TYPE,
        CAST(COUNT(TYPE) AS FLOAT) AS TOTAL_COUNTS
    FROM FACEBOOK_COMPLAINTS
    GROUP BY TYPE
),
CTE3 AS (
    SELECT
        CTE1.TYPE,
        CTE1.PROCESSED_COUNTS,
        CTE2.TOTAL_COUNTS
    FROM CTE1 INNER JOIN CTE2
    ON CTE1.TYPE = CTE2.TYPE
)

SELECT 
    TYPE,
    CAST(PROCESSED_COUNTS / TOTAL_COUNTS AS FLOAT)
FROM CTE3
;

-----------------------------------------------------------------

-- Improved solution (obtained from ChatGPT) = 0.01804 seconds
SELECT 
    TYPE,
    ROUND(
        SUM(CASE WHEN PROCESSED = 'TRUE' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 
        2
    ) AS processed_rate
FROM FACEBOOK_COMPLAINTS
GROUP BY TYPE;
