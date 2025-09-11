## timeout issue

```
SHOW VARIABLES LIKE 'wait_timeout';
SET GLOBAL wait_timeout = 28800;  -- or higher
```

my.cnf
```
SET GLOBAL max_allowed_packet = 64*1024*1024;
```


## check recently changed tables

```sql
SELECT table_schema, table_name, create_time, update_time
FROM information_schema.tables
WHERE table_schema NOT IN ('mysql','information_schema','performance_schema','sys')
AND table_schema = '<schema>';
```
