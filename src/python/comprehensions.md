## comprehensions

```python
[fn(i) for i in list]            # .map
map(fn, list)                    # .map, returns iterator

filter(fn, list)                 # .filter, returns iterator
[fn(i) for i in list if i > 0]   # .filter.map
```