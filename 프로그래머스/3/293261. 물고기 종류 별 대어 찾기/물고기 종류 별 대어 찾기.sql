-- 코드를 작성해주세요
select ID, FISH_NAME, tmp.LENGTH as LENGTH from fish_info a
    left join fish_name_info b on a.fish_type=b.fish_type
    inner join (select fish_type, max(length) LENGTH from fish_info
        group by fish_type) tmp
        on a.fish_type=tmp.fish_type and a.LENGTH=tmp.LENGTH
    
    