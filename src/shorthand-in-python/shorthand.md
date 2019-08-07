# Writing shorthand statements in python

Python is having  shorthand statements and shorthand operators. These things will help you write more logic with less number of statements.

We will see those available shorthand statements.


## lambda statement

Probably every body is aware of the lambda functions. The statement lambda is helpful to write single line functions with out naming a function. This will return the function reference where you can assign it to any arbitrary variable. It's more like JavaScript anonymous functions.

```python
foo = lambda a: a+3
foo(3)
6
foo(8)
11
```


## SELF CALLED LAMBDA

You can write the lambda and you can make it call it self like self-invoking functions in javascript. Let's see an example.

```python
(lambda a: a+3)(8)
11
(lambda x: x**x)(3)
27
```


## List Comprehension

List Comprehension is the great feature that python is having. Using this feature you can reduce the lot of code, you can reduces space complexity of the code. Simple for loops can be written using list comprehension.

> Syntax:
> 
> **L** = **[** mapping-expression **for** element **in** source-list **if** filter-expression **]**
> 
> Where:
> 
> **L**       Variable, result gets assigned to
> 
> **mapping-expression**       Expression, which is executed on every loop if only filter-expression > in if condition resolved as True
> 
> This list comprehension is equivalent to.

```python
result = []
for element in source-list:
  if filter-expression:
    result.append(mapping-expression)
```

### EXAMPLE

Lets see list comprehension example. Get even number from the given range.

- Usual code

```python
result = []
for i in range(10):
  if i%2 == 0:
    result.append(i)

print(result)
[0, 2, 4, 6, 8]
```

- List Comprehension

```python
[i for i in range(10) if i%2==0]
[0, 2, 4, 6, 8]
```


## Dict Comprehension

Dict comprehension is available in python 2.7 and 3.x. This syntax will provide you the way to encapsulate several lines you use to create dictionaries into one line. It's is similar to list comprehension but we use dict literals {} instead of [].

> Syntax:
>
> {**key**:**value** for **element** in **source-list** if **filter-expression** }

Let's how we use it by an example.

I have a list of fruits, I want to make it dictionary by changing their case

['APPLE', 'MANGO', 'ORANGE']

I want to convert all keys into lower case. This is we would do with out using comprehension.

```python
l = ['MANGO', 'APPLE', 'ORANGE']

d = {}

for i in l:
  d[i.upper()] = 1

{'ORANGE': 1, 'MANGO': 1, 'APPLE': 1}
```

Using Simple list comprehension.

```python
{i.upper(): 1 for i in l}
```


## Set Comprehension

Set comprehension syntax is very much similar to dict comprehension with a small difference.

Let’s consider dict comprehension example. Using following statement you generate set

```python
{i.upper() for i in l}
```

Where we haven’t specified value like we do in dict comprehension


## Generator Expression

You might have already know about generators. Any function which contains yield statment is called generator. generator gives iterable where we can call next method to get the next item in the sequence.  Python got short notation for this generators like lambda. It is same as list comprehension but we enclose the expression with touple literals instead.

- GENERATOR FUNCTION

```python
def gen():
  for i in range(10):
    yield i 
g = gen()
<generator object gen at 0x7f60fa104410>
g.next()
0
g.next()
1
```

- GENERATOR EXPRESSION

Same generator function can written as follow.

```python
g = (i for i in range(10))
g
<generator object <genexpr> at 0x7f60fa1045f0>
g.next()
0
```


## Shorthand If Else

Like C and javascript ternary operator (?:) you can write short hand if-else comparison. By taking readability into account we have following syntax in python

**if-expression** if **(condition)** else **else-expression**

This is equivalent to.

```python
if True:
  print("This is True")
else:
  print("This is False")
```


## Tuple Unpacking

Python 3 even more powerful unpacking feature. Here it is.

Example:

```python
a, rest = [1, 3, 4, 6]
```

In this case, a will get 1   and rest of the list will get assigned to variable rest. i.e  [3, 4, 6]


## String Concatenation  with delimiter

If you want to concatenate list of strings with some random delimiter. You can do that by using string method **join**


```python
" || ".join(["hello", "world", "how", "are", "you"])

'hello || world || how || are || you'
```