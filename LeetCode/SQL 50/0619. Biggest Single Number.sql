(
    select
    num from mynumbers
    group by num
    having count(num) = 1
    order by num desc limit 1
)
union all
(
    select null
)
limit 1
;