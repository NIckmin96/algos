-- 코드를 입력하세요
select warehouse_id, warehouse_name, address, ifnull(freezer_yn, 'N') as freezer_yn from food_warehouse
# SELECT warehouse_id, IFNULL(warehouse_name),warehouse_name as warehouse_name, address, freezer_yn from food_warehouse
    where address like "경기도%"
    order by warehouse_id