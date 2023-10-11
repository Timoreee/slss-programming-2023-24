---
tags:
  - notes
  - natural-language-programming
  - y2023
  - programming-level-2
---
# Natural Language Processing
## Output
we can use a function to display text and symbols to the screen
we can use the `print()` function to display output

```python
print("Your text goes in here.")
```

## [[Headers]]

## Comments
Comments are pieces of text that are not interpreted by python
This means that the text is ignored.
We use the # symbol to make comments


```python
# This is a comment
```

# Input
we can grab information from the user using the input( ).
When we run the function, it does two things:
1. It waits for the user to write something or nothing
2. The user presses Enter/Return to indicate that they are finished

```python
input()

input(<prompt>) # Prints out a prompt then waits
```

# Variables
variables allow us to store information for the time that our app is running

```python
favourite_food = input("What is your favourite food?")
```

favourite food -> name of the variable
= -> assignment operator
input... -> value
# Naming
What you can do:
1. name them with letters, numbers, and underscores
2. names **should** start with a lowercase letter
What you can't do
1. you **can't** name them with spaces or symbols
2. you **can't**** name them with certain names that are reserved
	1. e.g. if, while, for, and, or, ...

A good name is something like this: 
```python
favourite_food
fave_food
date_of_birth
student_number
```

Bad names are like this:
```python
a
num
aa
aaa
aaaaa
```
# [[Strings]]
if we want to evaluate in a string we use f-strings.
To create an f-string, we put an f before the open quote

```python
fave_food = input("What's your favorite food?")

print(f"Oooooooo, {fave_food} sounds good!"")
```
# String Methods

[[Methods]] are functions that we can use on [[objects]].

String methods allow us to modify strings.

Say for example, we want ot make all od the characters of a string lowercase

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower()

```
```
# [[Design]]
*The Design Process* is the steps that we take when we create a solution to a problem

There are four steps in our design process
## 1.  Design out Algorithm in English (or any human language)
an **algorithm **is a sequence of steps to solve a problem
in this class, before we start ANY programming, we write our steps in English

## 2. Translate out Algorithm from English to Python
We'll translate our  algorithm into "proper" Python

## 3. Test our Python Algorithm
Check if it works *syntatically*, in other words, we check to see if it BREAKS
Check if it works *semantically*, in other words, we ask does our algorithm actually solve the problem

## 4. Share our work
Once it solves the problem, ship your code to whoever will use it


# Lists
a list in python is a collection of items 
We can store *different* values in a list
**Order Matters** in a list
# Creating A list
to make a list, we use brackets \[\] to surround our list
We separate out the items using ,

```python
some_list - ["Matt", "Ethan", "Johanne"]
```
The lower.() method takes a string and converts all uppercase letters into lower case.
# Access Elements in a List
We can grab things from lists using the bracket notation "Tim", I would do the following

```python
some_list[1].      # "Ethan"
some_list[2].      # "Johanne"
some_list[-1].     # "Johanne"
some_list[-2]      # "Ethan"
```

Inside the brackets we say the *index* of the value we want
Python uses *0-index* counting, which means we start counting at 0

# Modules
Modules are bits of code that we can use in Python
These bits of code aren't automatically included, so we need to import them into our code

# Boolean

# Conditionals

# Import
The  `import` keyword loads the module into our file `import` should be at the **top of the file** under the **header**
# The `time` module
Time allows us to play around with anything relating to `time`

```python
import time

# Pause code for 1 second
time.sleep[1]
```

# Iteration
![Loop from Giphy](https://media1.giphy.com/media/6HsjDOBPwY1eIS6kE0/giphy.gif?cid=ecf05e47u4wu0hvl9m1juhmryx7t9tw7httc7qnwe9k8shyg&ep=v1_gifs_search&rid=giphy.gif&ct=g)

  

We can repeat our instructions using *_iteration_* or *_loops_*.

  

More detailed information can be found [here](https://runestone.academy/ns/books/published/thinkcspy/Strings/TraversalandtheforLoopByItem.html). 

## Iterating over a [[List]]

  

Say, for example, we want to repeat instructions for all items inside of a list. Python has a way that we can do this.

  

```python

for <item> in <list>:

<code block>

```

  

We can use the rules above to iterate over a list, that is, repeat the code block for every `item` in the list.

  

Think of it this way. We have a list of groceries below. As you can see, Mr. Ubial has his priorities straight.

  

```python

groceries = ["hot wheels", "ice cream", "video games"]

```

  

What if you wanted to print out a formatted version of the list, something useful like putting a bullet in front of the item and putting everything on a new line.

  

We could do something like this:

  

```python

for item in groceries:

print(f"* {item}")

print("---")

```

  

Which would output this:

  

```console

* hotwheels

---

* ice cream

---

* video games

---

```

  

If we imagine that we're looping through every item in the list, the `<item>` name represents that individual item.

## Search - A Practical Example

  

We can implement a basic type of search algorithm using loops, one is called [linear search](https://en.wikipedia.org/wiki/Linear_search).

  

It goes something like this:

  

```pseudocodeish

for <item> in <list>:

if <item> == <item you want to find>:

<do something with the item>

```

  

Here's a practical example. Let's say that we're looking to see if Jasmine Soto is in the list. We can do this:

  

```python

names = ['Elizabeth Singleton', 'Raymond Mitchell', 'Steven Murphy', 'Daniel Terry', 'Glenn Fisher', 'Jasmine Soto', 'Deborah Hicks', 'Beverly Ryan', 'Jason Smith', 'Jason Washington']

  

for name in names:

if name == "Jasmine Soto":

print("We found her!")

```

We can use string methods to help solve [Errors#Semantic Errors[semantic errors]]
# .lower()

the `.lower()` converts all uppercase letters into loercase
# .upper()

The `.upper()` method uppercases all letters

# .strip(chars)

The `.strip()` method removes characters from both the beginning and end of the string

```python
user_feeling = input("How are you feeling today?")

# "good!" "good." "Good!" "Goooooood!!!!!!"
if user_feeling.lower.strip("!.,") == "good":
	print("That's great!"
```

## .split(str)
The `.split()` method splits a string into a list, separating the string based on the characters you give it.

```python
grocery_string = "eggs milk cheese hotwheels"

grocery_list = grocery_str.split("")
```