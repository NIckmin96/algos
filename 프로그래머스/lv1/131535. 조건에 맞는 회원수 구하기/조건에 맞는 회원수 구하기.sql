-- 코드를 입력하세요
SELECT count(user_id) as users from user_info
    where DATE_FORMAT(JOINED, "%Y-%m-%d") like "2021%"
    and (AGE >= 20 and AGE <= 29)