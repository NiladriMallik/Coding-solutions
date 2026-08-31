SELECT
  ad_campaign,
  COUNT(impression_id) AS impressions,
  SUM(revenue) AS total_revenue,
  ROUND(100 * SUM(clicked) / COUNT(*), 1) AS ctr
FROM ad_impressions
GROUP BY ad_campaign
HAVING impressions > 5
ORDER BY ctr DESC