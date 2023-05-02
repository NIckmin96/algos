-- 코드를 입력하세요
SELECT a.product_code, sum(a.price * b.sales_amount) as sales from product as a
    inner join offline_sale as b
        on a.product_id = b.product_id
    group by a.product_id
    order by sales desc, product_code asc