#!/usr/bin/python

# set
set1 = {"Weimann", "Dickens", "Lakin"}

print(set1)
# output:
# {'Weimann', 'Lakin', 'Dickens'}



# check if "Weimann" is present in the set
set2 = {"Weimann", "Dickens", "Lakin"}

print("Weimann" in set2)
# output:
# True



# add
set3 = {"Weimann", "Dickens", "Lakin"}

set3.add("Schneider")

print(set3)
# output:
# {'Lakin', 'Dickens', 'Schneider', 'Weimann'}



# add multiple items to a set
set4 = {"Weimann", "Dickens", "Lakin"}

set4.update(["Schneider", "Kshlerin", "Pfannerstill"])

print(set4)
# output:
# {'Dickens', 'Kshlerin', 'Schneider', 'Weimann', 'Lakin', 'Pfannerstill'}



# get the length of a set
set5 = {"Weimann", "Dickens", "Lakin"}

print(len(set5))
# output:
# 3


# remove
set6 = {"Weimann", "Dickens", "Lakin"}

set6.remove("Dickens")

print(set6)
# output:
# {'Lakin', 'Weimann'}



# clear
set7 = {"Weimann", "Dickens", "Lakin"}

set7.clear()

print(set7)
# output
# set()



# del
set8 = {"Weimann", "Dickens", "Lakin"}

del set8

try:
  print(set8)
except:
  print("Not found")

# output:
# Not found



# set constructor
set9 = set(("Weimann", "Dickens", "Lakin"))

print(set9)

# output:
# {'Weimann', 'Dickens', 'Lakin'}