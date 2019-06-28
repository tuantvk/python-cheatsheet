## lists

```python
list = []  # list empty
list[i:j]  # returns list subset
list[-1]   # returns last element
list[:-1]  # returns all but the last element

list[i] = val
list[i:j] = otherlist  # replace ith to jth element with otherlist
del list[i:j]

list.append(item)
list.extend(another_list)
list.insert(index, item)
list.pop()        # returns and removes last element from the list
list.pop(i)       # returns and removes i-th element from the list
list.remove(i)    # removes the first item from the list whose value is i
list1 + list2     # combine two list    
set(list)         # remove duplicate elements from a list

list.reverse()    # reverses the elements of the list in-place
list.count(item)
sum(list)

zip(list1, list2)  # returns list of tuples with n-th element of both list1 and list2
list.sort()        # sorts in-place, returns None
sorted(list)       # returns sorted copy of list
",".join(list)     # returns a string with list elements seperated by comma
```