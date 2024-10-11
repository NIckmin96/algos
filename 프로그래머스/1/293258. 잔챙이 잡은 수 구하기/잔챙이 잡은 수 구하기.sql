-- 코드를 작성해주세요
SELECT count(distinct(id)) as 'FISH_COUNT' FROM FISH_INFO
    where LENGTH is NULL
    