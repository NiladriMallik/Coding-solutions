SELECT
  YEAR(bill_date) AS fiscal_year,
  ROUND(SUM(amount), 2) AS total_spend,
  COUNT(DISTINCT svc_name) AS service_count
FROM cloud_costs
GROUP BY fiscal_year