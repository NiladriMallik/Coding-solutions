SELECT
  COUNT(DISTINCT u.user_id) AS active_users_with_transactions
FROM users AS u
INNER JOIN transactions AS t
  ON u.user_id = t.user_id
WHERE MONTH(t.transaction_date) = '04'
AND YEAR(t.transaction_date) = '2026'
AND u.account_status = 'active'