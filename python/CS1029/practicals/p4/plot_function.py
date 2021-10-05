import matplotlib.pyplot as plt
import numpy as np

# get the value for x = [ 0,1, 2, 3, 4]
x = [i for i in range(-5, 6)]

# calculate y = x^2
y = np.array(x) ** 2

# do a scatter plot of y vs x
plt.scatter(x, y, color='green')
plt.show()