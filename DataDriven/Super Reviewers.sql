SELECT
    reviewer,
    count(review_id) AS review_count
FROM code_reviews
WHERE merged IS NOT NULL
GROUP BY reviewer
HAVING REVIEW_COUNT > 24
ORDER BY count(review_id) DESC
;