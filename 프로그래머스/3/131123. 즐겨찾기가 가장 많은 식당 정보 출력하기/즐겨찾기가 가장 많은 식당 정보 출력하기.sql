-- 코드를 입력하세요
select a.food_type, a.rest_id, a.rest_name, a.favorites from rest_info a
    inner join (SELECT food_type, max(favorites) favorites from rest_info
    group by food_type) b
    on a.food_type=b.food_type and a.favorites=b.favorites
    order by food_type desc
