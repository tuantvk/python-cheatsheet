#!/usr/bin/python

# list
list1 = ["one", "two", "three"]

print(list1)
# output:
# ["one", "two", "three"]



# access items
list2 = ["one", "two", "three"]

print(list2[1])
# output:
# two



# change item value
list3 = ["one", "two", "three"]

list3[1] = "four"

print(list3)
# output:
# ['one', 'four', 'three']



# for loop
list4 = ["one", "two", "three"]

for i in list4:
  print(i)

# output:
# one
# two
# three



# list length
list5 = ["one", "two", "three"]

print(len(list5))
# output:
# 3



# add item
list6 = ["one", "two", "three"]

list6.append("four")

print(list6)
# output:
# ['one', 'two', 'three', 'four']



# insert
list7 = ["one", "two", "three"]

list7.insert(1, "four")

print(list7)
# output:
# ['one', 'four', 'two', 'three']



# remove
list8 = ["one", "two", "three"]

list8.remove("two")

print(list8)
# output:
# ['one', 'three']



# pop
list9 = ["one", "two", "three"]

list9.pop()

print(list9)
# output
# ['one', 'two']



# del
list10 = ["one", "two", "three"]

del list10[1]

print(list10)
# output:
# ['one', 'three']



# list
print(list(("one", "two", "three")))
# output:
# ['one', 'two', 'three']