-- 코드를 입력하세요
# BETWEEEN : 두 기간 사이의 데이터 조회 / HOUR : 시간 추출 함수
select HOUR(datetime) as hour, count(animal_id) from animal_outs
    group by hour
        having hour >= 9 and hour < 20
    order by hour