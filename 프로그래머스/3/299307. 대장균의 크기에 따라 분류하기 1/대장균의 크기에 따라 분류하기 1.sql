-- 코드를 작성해주세요
SELECT ID, IF (size_of_colony<=100, 'LOW', if(size_of_colony<=1000, 'MEDIUM','HIGH')) as 'SIZE' FROM ECOLI_DATA
order by 1 asc;