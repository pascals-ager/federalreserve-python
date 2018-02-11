
select extract(year from period) as year, avg(data) as yearly_unemp_rate
from fred.unemployment_rate_stg 
where year >= '01-01-1980' and year < '31-12-2015'
group by 1 
order by year;
