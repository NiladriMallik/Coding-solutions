--Runtime 528 ms, beats 99.78% of other submissions

SELECT
    USER_ID,
    CONCAT(UPPER(SUBSTR(NAME, 1, 1)), LOWER(SUBSTR(NAME,2))) AS NAME
FROM USERS
ORDER BY USER_ID;