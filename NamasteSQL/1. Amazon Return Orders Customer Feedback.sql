select
	o.customer_name,
	cast(count(r.order_id) * 100.0 / count(*) as decimal (5,  2)) as return_percent
from orders o left join returns r
on o.order_id = r.order_id
group by o.customer_name
having count(r.order_id) * 100.0 / count(*) > 50
order by o.customer_name asc
;