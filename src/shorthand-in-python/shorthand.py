# shorthand in python example
# note: use python 3+


# lambda statement

foo = lambda a: a+3
print(foo(3))
print(foo(8))

# output:
# 6
# 11


# SELF CALLED LAMBDA

print((lambda a: a+3)(8))
print((lambda x: x**x)(3))

# output:
# 11
# 27


# List Comprehension

result = []
for i in range(10):
  if i%2 == 0:
    result.append(i)

print(result)

# output:
# [0, 2, 4, 6, 8]

print([i for i in range(10) if i%2==0])

# output:
# [0, 2, 4, 6, 8]


# Dict Comprehension

l = ['MANGO', 'APPLE', 'ORANGE']

d = {}

for i in l:
  d[i.upper()] = 1

print(d)

# output:
# {'MANGO': 1, 'APPLE': 1, 'ORANGE': 1}

print({i.upper(): 1 for i in l})

# output:
# {'MANGO': 1, 'APPLE': 1, 'ORANGE': 1}