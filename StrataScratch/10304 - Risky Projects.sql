-- My solution

with cte1 as(
    select
        le.salary as emp_salary,
        lp.title as proj_title,
        lp.budget as proj_budget,
        datediff(day, lp.start_date, lp.end_date) as proj_duration_in_days
    from linkedin_employees le
    left join linkedin_emp_projects lep on le.id = lep.emp_id
    left join linkedin_projects lp on lep.project_id = lp.id
),

cte2 as(
    select
        proj_title as title,
        proj_budget as budget,
        ceiling(sum(emp_salary / 365.0 * (proj_duration_in_days))) as prorated_employee_expense
    from cte1
    group by proj_title, proj_budget, proj_duration_in_days
)
select * from cte2
where budget < prorated_employee_expense

-- Optimized solution
with cte1 as(
    select
        lp.title as proj_title,
        lp.budget as budget,
        ceiling(sum(le.salary / 365.0 * (datediff(day, lp.start_date, lp.end_date)))) as prorated_employee_expense
    from linkedin_employees le
    left join linkedin_emp_projects lep on le.id = lep.emp_id
    left join linkedin_projects lp on lep.project_id = lp.id
    group by lp.title, lp.budget, lp.start_date, lp.end_date
)

select * from cte1
where budget < prorated_employee_expense