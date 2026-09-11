select
    distinct region
from orders
where profit > 1200
and region is not null
and region not in (select distinct country from customers)
and status in ('Shipped', 'Completed')
order by region asc
;