SELECT
  CASE
    WHEN severity IS NULL THEN 'unknown'
    ELSE severity
  END AS severity,
  COUNT(alert_id) AS alert_count
FROM alert_events
GROUP BY severity
ORDER BY alert_count DESC