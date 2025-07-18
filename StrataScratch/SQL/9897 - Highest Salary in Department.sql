SELECT DEPARTMENT, FIRST_NAME, SALARY FROM (
    SELECT
        FIRST_NAME,
        DEPARTMENT,
        SALARY,
        RANK() OVER (PARTITION BY DEPARTMENT ORDER BY SALARY DESC) AS SALARY_RANK
    FROM EMPLOYEE
)E
WHERE SALARY_RANK = 1
;