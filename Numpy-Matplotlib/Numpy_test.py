#!/usr/bin/env python3

import numpy as np

x = [5, 10, 15, 20, 25]

# declare y as an empty list
y = []

# Like C/C++
for counter in x:
   y.append(counter / 5)

print("\nOld fashioned way: x = {} y = {} \n".format(x, y))

# Now using List of comprehension
z = [n/5 for n in x]

print("List Comprehensions: x = {} z = {} \n".format(x, z))

# This doesn't work with common lists.
print("Trying to divide a list !")
try:
    a = x / 5
except:
    print("No, you can't do that with regular Python lists\n")
    print("REMEBER:You can't divide a list directly\n")

# Now using Numpy :D
a = np.array(x)
b = a / 5

print("With Numpy - Array: a = {} b = {} \n".format(a, b))