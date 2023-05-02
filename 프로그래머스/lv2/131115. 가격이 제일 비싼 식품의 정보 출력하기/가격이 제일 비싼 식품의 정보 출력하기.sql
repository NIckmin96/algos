-- 코드를 입력하세요
select * from food_product as a
    where a.price = (SELECT max(price) from food_product)