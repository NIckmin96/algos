-- 코드를 입력하세요
# with tmp as(SELECT * from animal_ins ins
#     left outer join animal_outs outs on ins.animal_id=outs.animal_id
# union
# SELECT * from animal_ins ins
#     right outer join animal_outs outs on ins.animal_id=outs.animal_id)
    
SELECT outs.animal_id, outs.name from animal_ins ins
    left outer join animal_outs outs on ins.animal_id=outs.animal_id
    where ins.datetime is null and outs.datetime is not null
union
SELECT outs.animal_id, outs.name from animal_ins ins
    right outer join animal_outs outs on ins.animal_id=outs.animal_id
    where ins.datetime is null and outs.datetime is not null
order by animal_id
    
    