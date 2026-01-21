WITH CTE1 AS(
    SELECT
        CUST_ID,
        STATE,
        TIMESTAMP,
        SUM(
            CASE
                WHEN STATE = 0 THEN DATEDIFF(
                    MINUTE,
                    LAG(TIMESTAMP, 1) OVER (PARTITION BY CUST_ID ORDER BY TIMESTAMP ASC),
                    TIMESTAMP
                )
                ELSE 0
            END
        ) / 60.0
        AS HOURS
    FROM CUST_TRACKING
)
SELECT
    CUST_ID,
    SUM(HOURS)/60.0 AS TOTAL_TIME
FROM CTE1
GROUP BY CUST_ID
ORDER BY CUST_ID ASC
;