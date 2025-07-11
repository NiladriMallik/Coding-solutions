SELECT DISTINCT USER_ID FROM(
    SELECT
        USER_ID,
        DATEDIFF(DAY, LAG(CREATED_AT, 1) OVER (PARTITION BY USER_ID ORDER BY CREATED_AT), CREATED_AT) AS DAY_DIFFS
    FROM AMAZON_TRANSACTIONS
) e
WHERE DAY_DIFFS IS NOT NULL AND DAY_DIFFS <= 7
ORDER BY USER_ID ASC
;