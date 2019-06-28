## dict

```python
dict.keys()
dict.values()
"key" in dict    # let's say this returns False, then...
dict["key"]      # ...this raises KeyError
dict.get("key")  # ...this returns None
dict.setdefault("key", 1)
```