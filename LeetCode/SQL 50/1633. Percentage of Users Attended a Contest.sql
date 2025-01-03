with cte1 as(
    select
    r.contest_id,
    u.user_id
    from users u right join register r on u.user_id = r.user_id
),

cte2 as(
    select contest_id,
    (count(user_id) over (partition by contest_id)) as participated
    from cte1
)


select 
distinct contest_id, 
round(participated/(select count(user_id) from users) * 100, 2) as percentage
from cte2
group by contest_id
order by percentage desc, contest_id asc;