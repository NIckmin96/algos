-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, if(status='SALE','판매중',if(status='RESERVED','예약중','거래완료')) STATUS from used_goods_board
    where created_date=date_format('2022-10-05','%Y-%m-%d')
    order by board_id desc