/* Write your T-SQL query statement below */
with cte1 as(
    select *,
    lag(temperature, 1) over(order by recordDate asc) as prev_temp,
    lag(recordDate, 1) over(order by recordDate asc) as prev_record_date
    from weather
    order by recordDate asc  
),
cte2 as(
    select *,
    datediff(recordDate, prev_record_date) as daydiff
    from cte1
)
select
id
from cte2
where temperature > prev_temp and daydiff = 1
;