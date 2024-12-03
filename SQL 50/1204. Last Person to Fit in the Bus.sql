--The following submission beat around 69% of all solutions, runtime is 883 ms.
SELECT 
PERSON_NAME FROM
(
    SELECT 
    *,
    LEAD(CUMUL_WEIGHT, 1) OVER(ORDER BY TURN) AS NEXT_WEIGHT
    FROM(
        SELECT
            PERSON_ID,
            PERSON_NAME,
            WEIGHT,
            TURN,
            SUM(WEIGHT) OVER (ORDER BY TURN) AS CUMUL_WEIGHT
        FROM QUEUE
        ORDER BY TURN ASC
    ) E
) F
WHERE CUMUL_WEIGHT <= 1000 AND (NEXT_WEIGHT > 1000 OR NEXT_WEIGHT IS NULL);

------------------------------------------------------------------------------------
--The following submission is my best solution, beat 78.70% of all solutions, runtime is 832 ms.
SELECT 
PERSON_NAME
FROM(
    SELECT
        PERSON_ID,
        PERSON_NAME,
        WEIGHT,
        TURN,
        SUM(WEIGHT) OVER (ORDER BY TURN) AS CUMUL_WEIGHT
    FROM QUEUE
    ORDER BY TURN ASC
) E
WHERE CUMUL_WEIGHT <= 1000
ORDER BY TURN DESC LIMIT 1;