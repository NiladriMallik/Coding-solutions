SELECT
  svc_name,
  severity,
  COUNT(alert_id) AS alert_count
FROM alert_events
GROUP BY svc_name, severity
ORDER BY alert_count DESC
;