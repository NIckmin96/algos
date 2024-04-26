-- 코드를 입력하세요
SELECT a.product_id, a.product_name, sum(price*amount) total_sales from food_product a
    inner join food_order b on a.product_id=b.product_id
    where year(b.produce_date)=2022 and month(b.produce_date)=5
    group by a.product_id
    order by total_sales desc, product_id asc
    