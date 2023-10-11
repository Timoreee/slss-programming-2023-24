---
tags:
  - slss
  - notes
  - y2023
  - programming-level-2
---
# Syntax Errors
These are types of errors are where you run your code and something breaks.

Syntax errors are pretty easy to fix
syntax errors happen when we don't follow the rules completely
some examples of syntax errors are when we are missing a closing parenthesis 

	Syntax <==> Rules
# Semantic Errors
Semantic errors are much harder to squash (in Mr. Ubials opinion).

Semantic errors are where your code doesn't "mean" what you actually mean

```python
user_response = input("Do you like to eat food?")

if user_response.lower() == "yes":
	print("You passed the human test.")
else:
	print("You must be some sort of Robot.")
```

The problem with the above code is subtle. What I(Mr. Ubial) mean is that if the user answers with ANYTHING affirmative, the code should go into the "yes" block.

One way to solve this problem is to use [[Strings#String Methods]]. We can use`.lower` to catch all permutations of capital letters in the code
semantic errors are when your code doesnt mean what you actually want it to mean