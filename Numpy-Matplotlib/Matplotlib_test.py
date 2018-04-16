#!/usr/bin/env python3

import numpy as np
# This import only the pyplot library of matplotlib -> Saves memory !
import matplotlib.pyplot as plt

x = np.linspace(0,20,100)

#print("Linespace:x={}\n".format(x))

y1 = np.sin(x)
y2 = np.cos(x)

# Plot the sin and cos functions
plt.plot(x , y1, "-b", label="sine")
plt.plot(x , y2, "-r", label="cos")

# The legend should be in the top right corner
plt.legend(loc="upper right")

# Limit the y axis to -1.5 to 1.5
plt.ylim(-1.5, 1.5)
plt.show()

