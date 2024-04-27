-- 코드를 작성해주세요
/* 
1. left join
2. group by 물고기 종류
*/
select count(*) fish_count, fish_name from fish_info a
    left join fish_name_info b on a.fish_type=b.fish_type
    group by fish_name
    order by fish_count desc
    