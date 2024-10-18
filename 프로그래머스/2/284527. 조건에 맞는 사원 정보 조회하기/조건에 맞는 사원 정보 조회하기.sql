select a.score as score, a.emp_no, emp_name, position, email from
    (select sum(score) score, emp_no from hr_grade group by emp_no) a
    inner join hr_employees b
        on a.emp_no=b.emp_no
    order by score desc
    limit 1;