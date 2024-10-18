-- 코드를 작성해주세요
select id, email, first_name, last_name from developer_infos
    where 'Python' = SKILL_1
        or 'Python' = SKILL_2
        or 'Python' = SKILL_3
    order by id asc;