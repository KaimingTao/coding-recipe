## Count number of all files

```
find /path/to/folder -type f | wc -l
```

## Count total lines

```
find /path/to/folder -type f -exec wc -l {} + | awk '{total += $1} END {print total}'
```
