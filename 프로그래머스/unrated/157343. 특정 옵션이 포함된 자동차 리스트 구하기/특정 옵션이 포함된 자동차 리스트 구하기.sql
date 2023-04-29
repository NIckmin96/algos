-- 코드를 입력하세요
SELECT car_id, car_type, daily_fee, options from car_rental_company_car
    # 리스트값 중에 찾는 법 : LIKE
    where options like '%네비게이션%'
    order by car_id desc