## timeout issue

```
SHOW VARIABLES LIKE 'wait_timeout';
SET GLOBAL wait_timeout = 28800;  -- or higher
```

```
SET GLOBAL max_allowed_packet = 64*1024*1024;
```
