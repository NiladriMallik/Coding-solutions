SELECT
  user_id,
  COUNT(session_id) AS total_sessions
FROM user_sessions
GROUP BY user_id
HAVING COUNT(session_id) > (
  SELECT
    COUNT(session_id) / COUNT(DISTINCT 
      user_id
      ) AS avg_sessions
  FROM user_sessions
)