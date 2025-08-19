## find folder only has digits in name

```
find . -type d -regextype posix-egrep  -regex '.*/[0-9]{5,}$'
```
