-- 코드를 입력하세요
select user_id, nickname, concat(city, ' ', street_address1, ' ', street_address2) 전체주소, concat(substr(tlno,1,3),'-',substr(tlno,4,4),'-',substr(tlno,8,4)) 전화번호 from used_goods_user a
    inner join (SELECT distinct(writer_id) from used_goods_board
    group by writer_id
    having count(contents)>=3) b 
    on a.user_id=b.writer_id
    order by user_id desc
