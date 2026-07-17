select
    distinct
    p.post_date,
    p.post_id,
    p.post_keywords,
    p.post_text,
    p.poster
from facebook_posts p left join facebook_reactions r
on r.post_id = p.post_id
where r.reaction = 'heart'