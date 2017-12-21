
select avg(data) 
from fred.unemployment_rate_stg 
where period >= '1980-01-01 00:00:00'::timestamp 
and period <= '2015-01-01 00:00:00'::timestamp;
