-- 코드를 작성해주세요
select DISTINCT(a.item_id) as 'ITEM_ID', ITEM_NAME from item_info a
    inner join item_tree b on a.ITEM_ID = b.ITEM_ID
    where parent_item_id is null
    