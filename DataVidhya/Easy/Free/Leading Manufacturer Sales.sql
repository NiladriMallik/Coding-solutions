-- Write query here
-- MODEL NAME: `tms_pharma_in`

SELECT
    manufacturer,
    CONCAT('$', CAST(ROUND(SUM(total_sales) / 1000000.0) AS VARCHAR), ' million') AS sale
FROM  {{ ref('tms_pharma_in') }}
GROUP BY manufacturer
ORDER BY SUM(total_sales) DESC, manufacturer
;