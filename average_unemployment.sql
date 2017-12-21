
select extract(year from period) as year, avg(data) as yearly_unemp_rate
from fred.unemployment_rate_stg 
group by 1 
having  extract(year from period) >= '1980'  
and extract(year from period) < '2015' 
order by year;
