SELECT DISTINCT
  u.username
FROM users AS u /* ,t.transaction_id, */ /* t.transaction_date, */ /* t.total_amount, */ /* us.session_id, */ /* us.session_duration_sec */
LEFT JOIN transactions AS t
  ON u.user_id = t.user_id
LEFT JOIN user_sessions AS us
  ON u.user_id = us.user_id
WHERE us.session_duration_sec IS NOT NULL
AND t.total_amount IS NOT NULL