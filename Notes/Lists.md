
# 2 Dimensional lists

so far, all the lists we've used in the class are one-dimensional
```python
some_list = ["red", "green", "blue"]

```

we can create two-dimensional lists, which are lists inside of a list

```python
some_2d_list = [
		[1, 2, 3], 
		[4, 5, 6], 
		[7, 8, 9]
]

#.           r  c
some_2d_list[0][0]        # -> 1
some_2d_list[-1][-1]      # -> 9
```

# Tuples

Tuples(toopulls or tuhpulls) are like lists except for one main thing

Tuples are **immutable**. immutable means that you can't change it.
This just means, simply, that you can't change the things inside of a tuple

```python
some_tuple = (1, 2, 3, 4, 5, 6)

some_tuple[0] # -> 1
```

Because tuples are immutable, you might think that this is a disadvantage. But because they are immutable this makes tuple

# Images and Tuples

The basic unit of measurement in images is a pixel. A pixel's information is stored in a tuple(3-tuple, a tuple of three values)

The 2-tuple tells us for ONE PIXEL, what the RED, GREEN, and BLUE values are


```python
			 r      g        b
RED =      (255,    0,       0)
GREEN =    (  0,   255,      0)
BLUE =     (  0,     0,     255)
WHITE =    ( 255,   255,     255 )
BLACK =    (  0,     0,       0)
GREY =     (   80,   80,      80)
```