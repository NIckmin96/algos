-- 코드를 입력하세요
SELECT book_id, author_name, date_format(published_date, "%Y-%m-%d") as published_date from book as b
    inner join author as a
        on b.author_id=a.author_id
    where category in ("경제")
    order by published_date