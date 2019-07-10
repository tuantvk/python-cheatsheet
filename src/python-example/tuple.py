#!/usr/bin/python

# tuple
tuple1 = ("html", "css", "javascript")

print(tuple1)
# output:
# ('html', 'css', 'javascript')



# access items
tuple2 = ("html", "css", "javascript")

print(tuple2[1])
# output:
# css



# for loop
tuple3 = ("html", "css", "javascript")

for x in tuple3:
  print(x)

# output:
# html
# css
# javascript



# tuple length
tuple4 = ("html", "css", "javascript")

print(len(tuple4))
# output:
# 3



# tuple
my_tuple = tuple(("html", "css", "javascript"))

print(my_tuple)
# output:
# ('html', 'css', 'javascript')


# remove
tuple5 = ("html", "css", "javascript")

del tuple5

try:
  print(tuple5)
except:
  print("'tuple5' is not defined")
  
# output:
# 'tuple5' is not defined