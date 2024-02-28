-- 코드를 입력하세요

SELECT order_id, product_id, date_format(out_date,'%Y-%m-%d') out_date, 
if(out_date<= str_to_date('20220501','%Y%m%d'), '출고완료', if(out_date>str_to_date('20220501','%Y%m%d'), '출고대기', '출고미정')) as 출고여부 from food_order
order by order_id asc