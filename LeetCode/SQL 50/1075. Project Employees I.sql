with cte1 as(
    select
    p.project_id,
    e.experience_years,
    round(avg(experience_years) over (partition by project_id), 2) as average_years
    from project p inner join employee e on p.employee_id = e.employee_id
)

select distinct project_id, average_years from cte1;