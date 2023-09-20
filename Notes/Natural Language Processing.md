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

# [[Strings]]
if we want to evaluate in a string we use f-strings.
To create an f-string, we put an f before the open quote

```python
fave_food = input("What's your favorite food?")

print(f"Oooooooo, {fave_food} sounds good!"")
```
