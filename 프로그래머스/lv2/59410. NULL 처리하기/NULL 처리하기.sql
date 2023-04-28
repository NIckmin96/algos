-- 코드를 입력하세요
SELECT animal_type, coalesce(name,"No name") as NAME, sex_upon_intake from animal_ins
order by animal_id