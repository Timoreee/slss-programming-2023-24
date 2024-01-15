In python, data can be grouped in categories called Types

| Name                   | Example                     |
| ---                    | ---                         |
| string                 | "hello"                     |
| list                   | [1, 2, 3, 4]                |
| integers or int        | 1, -10, 200, 69             |
| float                  |  3.5, 1.3, 1.0              |
| boolean or bool        | True False                  |
An example of using these types of data:

```python
favourite_food = "Tempura"
my_age = 16 # my age is of type int or integer
```

# Type Conversion
In Python, there are some special functions that allows us to change the type of something
```python
intro__string = "My age is".  # Type string
my_age = 15.                  # Type int

# Aside
"My name is" + "SlimShady"    # "My name isSlimShady

print(intro_string + my_age)  # THIS BREAKS!

```

We can fix the example this way 
```python
intro_string = "My age is"
my_age = 16

print(intro_string +str(my_age))        # "My age is16"
print(intro_string  " " + str(my_age))  # "My age is 16"
print(f"{intro_string} {my_age}"")      # "My age is 16"     

```