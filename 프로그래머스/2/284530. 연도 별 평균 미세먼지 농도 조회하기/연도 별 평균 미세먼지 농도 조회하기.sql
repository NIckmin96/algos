# select date_format(ym, '%Y') as YEAR, round(sum(pm_val1)/count(pm_val1), 2) as PM10, round(sum(pm_val2)/count(pm_val2),2) as 'PM2.5' from air_pollution
#     where location2='수원'
#     group by date_format(ym, '%Y')
#     order by YEAR asc

SELECT YEAR(ym) 'YEAR', round(avg(pm_val1), 2) as 'PM10', round(avg(pm_val2),2) as 'PM2.5' from AIR_POLLUTION
    where LOCATION2='수원'
    group by YEAR
    order by YEAR asc;