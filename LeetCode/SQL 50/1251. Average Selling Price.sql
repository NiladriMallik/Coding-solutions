with cte1 as(
    select 
    p.product_id,
    p.start_date,
    p.end_date,
    p.price,
    u.purchase_date,
    u.units
    from prices p left join unitssold u
    on p.product_id = u.product_id
    and u.purchase_date between p.start_date and p.end_date
),

cte2 as(
    select *,
    price * units / sum(units) over (partition by product_id) as average
    from cte1
),

cte3 as(
    select 
    product_id,
    start_date,
    end_date,
    purchase_date,
    round(sum(average) over (partition by product_id),2) as average_price
    from cte2
)
select 
    distinct product_id,
    case when average_price is null then 0 else average_price end as average_price
from cte3;