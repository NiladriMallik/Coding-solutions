WITH CTE1 AS(
    SELECT COUNT(USER_ID)
    FROM fb_active_users
    WHERE STATUS = 'open' 
    AND COUNTRY = "USA"
),

CTE2 AS(
    SELECT COUNT(*) FROM fb_active_users
)

SELECT (SELECT * FROM CTE1) / (SELECT * FROM CTE2)
;