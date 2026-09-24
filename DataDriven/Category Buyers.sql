select
    p.category,
    count(distinct t.user_id) as distinct_users,
    sum(t.total_amount) as total_revenue
from products p left join transactions t
on p.product_id = t.product_id
group by p.category
order by total_revenue desc
;