-- 코드를 입력하세요
SELECT user_id, b.nickname, sum(price) TOTAL_SALE from used_goods_board a
inner join used_goods_user b
    on writer_id=user_id
where a.status='DONE'
group by user_id
    having sum(price)>=700000
order by TOTAL_SALE asc

