from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

'''A linear regression example

This is a demon about linear regression
'''


X = np.array([1, 4, 7, 9]).reshape(4, 1)
# X = [[1, ], [4, ], [7, ], [9, ]]
y = [16, 64, 112, 133]

X_ = np.array([2, 3, 5, 6]).reshape(4, 1)
# X_ = [[2, ], [3, ], [5, ], [6, ]]

# we try to find out y = w_1 * x + w_0
# coef_ as (w_1,), intercept_ as w_0
# https://scikit-learn.org/stable/modules/linear_model.html

reg = linear_model.LinearRegression()
reg.fit(X, y)

# draw the training data
plt.scatter(X, y, color='green')
# draw the prediction for X_
plt.scatter(X_, reg.predict(X_), color='red')
# plot the solution we found
plt.plot(X, reg.predict(X), color='blue')
plt.show()
