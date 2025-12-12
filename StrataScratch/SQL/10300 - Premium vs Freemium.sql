-- My Solution
with cte1 as(
select
    ma.paying_customer,
    md.downloads,
    md.date
from ms_user_dimension mu inner join ms_acc_dimension ma
on mu.acc_id = ma.acc_id
left join ms_download_facts md
on mu.user_id = md.user_id
),

cte2 as(
    select
        date as download_date,
        sum(case when paying_customer = 'yes' then downloads else 0 end) as paying,
        sum(case when paying_customer = 'no' then downloads else 0 end) as non_paying
    from cte1
    group by date
)
select * from cte2
where non_paying > paying
order by download_date asc

--Optimized solution from ChatGPT
SELECT
    md.date AS download_date,
    SUM(CASE WHEN ma.paying_customer = 'yes' THEN md.downloads ELSE 0 END) AS paying,
    SUM(CASE WHEN ma.paying_customer = 'no'  THEN md.downloads ELSE 0 END) AS non_paying
FROM ms_user_dimension mu
JOIN ms_acc_dimension ma 
    ON mu.acc_id = ma.acc_id
LEFT JOIN ms_download_facts md
    ON mu.user_id = md.user_id
GROUP BY md.date
HAVING SUM(CASE WHEN ma.paying_customer = 'no' THEN md.downloads ELSE 0 END)
     > SUM(CASE WHEN ma.paying_customer = 'yes' THEN md.downloads ELSE 0 END)
ORDER BY download_date ASC;
