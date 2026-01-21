with cte1 as(
select
    o.nominee,
    sum(case when o.winner = 'FALSE' then 0 else 1 end) as total_winnings,
    n.top_genre
from oscar_nominees o right join nominee_information n
on o.id = n.id
group by o.nominee, n.top_genre
)

select top 1 top_genre from cte1
order by total_winnings desc
;

--Optimized solution
SELECT TOP 1 n.TOP_GENRE
FROM OSCAR_NOMINEES o JOIN NOMINEE_INFORMATION n
ON o.ID = n.ID
WHERE o.WINNER = 'TRUE'
GROUP BY n.TOP_GENRE
ORDER BY COUNT(*) DESC
;