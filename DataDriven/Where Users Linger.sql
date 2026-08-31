SELECT
  d.os_name,
  AVG(session_duration_sec) AS avg_duration
FROM user_sessions AS us
RIGHT JOIN devices AS d
  ON us.device_id = d.device_id
WHERE d.device_type = 'mobile'
GROUP BY d.os_name
ORDER BY avg_duration DESC
LIMIT 1