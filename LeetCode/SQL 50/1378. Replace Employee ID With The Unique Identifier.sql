/* Write your T-SQL query statement below */
select uni.unique_id, emp.name
from EmployeeUNI uni right join Employees emp
on emp.id = uni.id;