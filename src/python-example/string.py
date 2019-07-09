#!/usr/bin/python

str1 = 'Hello World!'
str2 = "I love Python"

print("str1[0]: ", str1[0])
print("str2[7:]: ", str2[7:])
# output:
# str1[0]:  H
# str2[7:]:  Python



# display multiline
str3 = """
Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s
"""

print("multiline", str3)
# output:
# Lorem Ipsum is simply dummy text of the printing 
# and typesetting industry. Lorem Ipsum has been the 
# industry's standard dummy text ever since the 1500s



# the len() method return the length of a string
str4 = "Example for length"

print("length", len(str4))
# output:
# length 18



# string in upper case or lower case
str5 = "I Love Python"

print("upper", str5.upper())
print("lower", str5.lower())
# output:
# upper I LOVE PYTHON
# lower i love python



# replace
str6 = "I Love Python"

print(str6.replace("o", "0"))
# output:
# I L0ve Pyth0n



# split
str7 = "I Love Python"

print(str7.split(" "))
# output:
# ['I', 'Love', 'Python']



# format
quantity = 3
price = 10

my_order = "I want {} item for {} dollars"

print(my_order.format(quantity, price))
# output:
# I want 3 item for 10 dollars



# strip, removes any whitespace from the beginning or the end
str8 = "   I Love Python   "

print(str8.strip())
# output:
# I Love Python