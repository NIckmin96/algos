-- 코드를 작성해주세요
select b.dept_id as 'DEPT_ID', dept_name_en, round(avg(sal),0) as 'AVG_SAL' from hr_department a
    right join hr_employees b on a.dept_id=b.dept_id
    group by b.dept_id
    order by AVG_SAL desc;