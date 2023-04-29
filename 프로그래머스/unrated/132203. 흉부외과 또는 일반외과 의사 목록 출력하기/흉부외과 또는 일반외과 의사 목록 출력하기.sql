-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, date_format(hire_ymd, "%Y-%m-%d") from doctor
    where mcdp_cd in ("CS","GS")
    # 다중 졍렬 조건
    order by hire_ymd desc, dr_name asc
