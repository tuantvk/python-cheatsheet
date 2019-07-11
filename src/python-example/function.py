#!/usr/bin/python

# function
def my_function():
  print("Hello world!")


# call function
def call_function():
  print("Hello world!")

call_function()

# output:
# Hello world!



# parameters
def pa_function(param):
  print("Hello", param)

pa_function("Emily")
pa_function("John")

# output:
# Hello Emily
# Hello John



# default parameters
def de_function(name = "Cat"):
  print("Hello" + name)

de_function()
de_function("Dog")

# output:
# Hello Cat
# Hello Dog



# return value
def ret_function(x):
  return x * 2

print(ret_function(5))
print(ret_function(6))
print(ret_function(2))

# output:
# 10
# 12
# 4



# recursion
def rec_function(x):
  if x > 0:
    result = x + rec_function(x - 1)
    print(result)
  else:
    result = 0
  return result

rec_function(5)

# output:
# 1
# 3
# 6
# 10
# 15



# passing a list as a parameter

numbers = ["one", "two", "three"]

def pas_function(x):
  for x in numbers:
    print("This is number", x)

pas_function(numbers)

# output:
# This is number one
# This is number two
# This is number three