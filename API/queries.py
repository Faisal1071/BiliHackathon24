class queries:
  hourly_query = """with ten_min_intervals as (
  select 
    (select min(timestmp)::date from sensordata) + ( n    || ' minutes')::interval start_time,
    (select min(timestmp)::date from sensordata) + ((n+10) || ' minutes')::interval end_time
  from generate_series(0, ((select max(timestmp)::date - min(timestmp)::date from sensordata) + 1)*24*60, 10) n
)
select f.start_time, f.end_time, avg(s.temperature) avg_val 
from sensordata s
right join ten_min_intervals f 
        on s.timestmp >= f.start_time and s.timestmp < f.end_time
where s.timestmp between now() + interval '1 HOURS' and now() + interval '2 HOURS'
group by f.start_time, f.end_time
order by f.start_time"""

  daily_query = """with hourly_min_intervals as (
  select 
    (select min(timestmp)::date from sensordata) + ( n    || ' minutes')::interval start_time,
    (select min(timestmp)::date from sensordata) + ((n+60) || ' minutes')::interval end_time
  from generate_series(0, ((select max(timestmp)::date - min(timestmp)::date from sensordata) + 1)*24*60, 60) n
)
select f.start_time, f.end_time, avg(s.temperature) avg_val 
from sensordata s
right join hourly_min_intervals f 
        on s.timestmp >= f.start_time and s.timestmp < f.end_time
where s.timestmp between now() - interval '23 HOURS' and now() + interval '2 HOURS'
group by f.start_time, f.end_time
order by f.start_time"""