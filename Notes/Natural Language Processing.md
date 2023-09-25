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
Once it solves the problem, ship your code to whoever will use it.