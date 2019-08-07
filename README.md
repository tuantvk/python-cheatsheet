# Python and Framework Cheatsheet

# Table of Content

1. [Lists](#1-lists)
2. [Dict](#2-dict)
3. [String](#3-string)
4. [Iteration](#4-iteration)
5. [Casting](#5-casting)
6. [Regex](#6-regex)
7. [Comprehdensions](#7-comprehdensions)
8. [Format date](#8-format-date)
9. [Django](#9-django)
10. [Example](#10-example)
11. [Contributing](#11-contributing)
12. [License](#12-license)

### Recommended
> Tips:
> View all my tools:
[All tools python](https://github.com/tuantvk/python-cheatsheet/tree/master/src/tools)

- **Tutorials**

  - [Learn Python | CodeAcademy](https://www.codecademy.com/learn/learn-python)
  - [Progate Python Classes](https://progate.com/languages/python)
  - [Video Tutorial for absolute beginners | YouTube](http://bit.ly/2NkrsKh)
  - [Intro to Python | Udacity](https://in.udacity.com/course/introduction-to-python--ud1110-india) :free:
  - [Python For Everybody](https://www.coursera.org/specializations/python)
  - [Write Better Python Functions](https://jeffknupp.com/)
  - [Learning Python: From Zero to Hero](https://medium.freecodecamp.org/learning-python-from-zero-to-hero-120ea540b567)
  - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) - Recommended
  - [The New Boston Python | Youtube](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_)
  - [Think Python 2e - Green Tea Press](http://greenteapress.com/thinkpython2/thinkpython2.pdf)
  - [A Byte of Python](https://python.swaroopch.com/)
  - [Project Euler](https://projecteuler.net/)
  - [A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
  - [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
  - [Python Class By Google](https://developers.google.com/edu/python/) - Recommended
  - [Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science)
  - [Python 3 for humans that want practical project exposure](https://pythonprogramming.net/)
  - [Learn Python the Hard Way](https://learnpythonthehardway.org/)

- **Django - Python**

  - [Try Django | YouTube](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW)
  - [Django Docs](https://docs.djangoproject.com/en/2.1/)
  - [Django Girls](https://tutorial.djangogirls.org/en/)
  - [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
  - [SimpleIsBetterThanComplex Blog](https://simpleisbetterthancomplex.com/)
  - [Tango With Django Book](https://www.tangowithdjango.com/book/)
  - [Django Class-Based Views](https://ccbv.co.uk/)
  - [The Algorithms Python](https://github.com/TheAlgorithms/Python)

- **Flask - Python**

  - [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

# Writing shorthand statements in python

Python is having  shorthand statements and shorthand operators. These things will help you write more logic with less number of statements.

We will see those available shorthand statements.

> File [Example shorthand.py](src/shorthand-in-python/shorthand.py)


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

## 1. Lists

![Lists](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/lists.png)

[Lists Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python/lists.md)

## 2. Dict

![Dict](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/dict.png)

[Dict Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python/dict.md)

## 3. String

![String](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/string.png)

[String Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python/string.md)

## 4. Iteration

![Iteration](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/iteration.png)

[Iteration Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python/iteration.md)

## 5. Casting

![Casting](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/casting.png)

[Casting Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python/casting.md)

## 6. Regex

![Regex](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/regex.png)

[Regex Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python/regex.md)

## 7. Comprehdensions

![Comprehdensions](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/comprehdensions.png)

[Comprehdensions Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python/comprehdensions.md)

## 8. Format date

![Format date](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/format-date.png)

[Format date Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python/format-date.md)

## 9. Django

[Django Cheatsheet](https://github.com/tuantvk/python-cheatsheet/blob/master/src/django/django-basic.md)

## 10. Example

#### Python example

- [string](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python-example/string.py)
- [list](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python-example/list.py)
- [tuple](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python-example/tuple.py)
- [function](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python-example/function.py)
- [set](https://github.com/tuantvk/python-cheatsheet/blob/master/src/python-example/set.py)


## 11. Contributing

So you want to contribute? Fun! I love seeing new PRs for python cheatsheet. If you are thinking about working on something, feel free to make an issue beforehand so that you can make sure it'll be worth your time!

> If you use screenshot code, plz resize image to 800.

> Try it:
[Resize image tool](https://github.com/tuantvk/python-cheatsheet/blob/master/assets/python/resize.py)

## 12. License

MIT