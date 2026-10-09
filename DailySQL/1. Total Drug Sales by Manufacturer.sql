-- Write your query for: 1. Total Drug Sales by Manufacturer
SELECT
    Manufacturer,
   concat('$', cast(sum(total_sales)/1000000 as int), ' million') as sale
FROM pharmacy_sales
group by Manufacturer
order by sale desc, Manufacturer asc
;