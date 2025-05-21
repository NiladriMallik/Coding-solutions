SELECT
    DISTINCT BUSINESS_NAME,
    CASE
        WHEN lower(BUSINESS_NAME) like '%restaurant%' THEN 'restaurant'
        WHEN LOWER(BUSINESS_NAME) like '%cafe%' 
            OR LOWER(BUSINESS_NAME) like '%café%'
            OR LOWER(BUSINESS_NAME) like '%coffee%'
        THEN 'cafe'
        WHEN LOWER(BUSINESS_NAME) LIKE '%school%' THEN 'school'
        ELSE 'other'
    END AS BUSINESS_TYPE
FROM SF_RESTAURANT_HEALTH_VIOLATIONS
;