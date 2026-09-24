SELECT
    distinct u.username
from users u left join search_queries s on u.user_id = s.user_id
left join page_views p on u.user_id = p.user_id
left join transactions t on u.user_id = t.user_id
where s.query_id is not NULL and p.view_id is not NULL and t.transaction_id is not NULL
order by u.username asc
;