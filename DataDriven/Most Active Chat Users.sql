with cte1 as(
    select
        sender_id,
        count(msg_id) as total_messages
    from chat_msgs
    group by sender_id
)

select
    dense_rank() over (order by total_messages desc) as rank,
    sender_id,
    total_messages
from cte1
;