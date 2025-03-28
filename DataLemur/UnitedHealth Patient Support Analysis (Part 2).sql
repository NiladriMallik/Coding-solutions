--PostgreSQL

SELECT 
  ROUND(
    (CAST(SUM(NA) AS FLOAT)/
    CAST(COUNT(*) AS FLOAT) * 100)::NUMERIC
    ,1)
FROM(
  SELECT
    CASE_ID,
    CALL_CATEGORY,
    CASE
      WHEN CALL_CATEGORY = 'n/a' OR CALL_CATEGORY IS NULL THEN 1
      ELSE 0
    END AS NA
  FROM CALLERS
)E
;