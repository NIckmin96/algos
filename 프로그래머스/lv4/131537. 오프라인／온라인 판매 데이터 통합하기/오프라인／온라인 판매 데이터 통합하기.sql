# -- 코드를 입력하세요
# (SELECT sales_date, product_id, user_id, sales_amount from online_sale as a
#     where sales_date like '2022-03%'
# union
# SELECT sales_date, product_id, NULL as user_id, sales_amount from offline_sale as b
#     where sales_date like '2022-03%')
# order by sales_date, product_id, user_id
    
(SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE AS N
WHERE SALES_DATE LIKE '2022-03%'
UNION
SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE AS F
WHERE SALES_DATE LIKE '2022-03%')
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID