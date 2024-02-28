-- 코드를 입력하세요
SELECT CATEGORY, sum(sales) TOTAL_SALES from BOOK_SALES a
inner join BOOK b
    on a.book_id=b.book_id
where sales_date like '2022-01%'
group by CATEGORY
order by CATEGORY ASC