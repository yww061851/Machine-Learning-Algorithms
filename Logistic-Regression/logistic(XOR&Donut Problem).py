# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:52:37 2016

@author: WYAO2
"""

"""
Donut Probelm and XOR problem
"""

import numpy as np
import matplotlib.pyplot as plt


"""
# The XOR problem
# Create a new dimension when the targers are not linearly separatable
"""
N = 4
D =2 
X = np.array([[0,0],[0,1],[1,0],[1,1]])
T = np.array([0,1,1,0])
ones = np.array([1]*N).T

xy = np.matrix(X[:,0]*X[:,1]).T
Xb = np.array(np.concatenate((ones, xy, X), axis=1))

# randomly initialize the weights
w = np.random.randn(D + 2)

# calculate the model output
z = Xb.dot(w)

def sigmoid(z):
    return 1/(1 + np.exp(-z))


Y = sigmoid(z)

# calculate the cross-entropy error
def cross_entropy(T, Y):
    E = 0
    for i in xrange(N):
        if T[i] == 1:
            E -= np.log(Y[i])
        else:
            E -= np.log(1 - Y[i])
    return E


# let's do gradient descent 100 times
learning_rate = 0.001
error = []
for i in xrange(5000):
    e = cross_entropy(T, Y)
    error.append(e)
    if i % 100 == 0:
        print (e)

    # gradient descent weight udpate with regularization
    w += learning_rate * ( np.dot((T - Y).T, Xb) - 0.01*w )

    # recalculate Y
    Y = sigmoid(Xb.dot(w))

plt.plot(error)
plt.title("Cross-entropy per iteration")
plt.show()

print ("Final w:", w)
print ("Final classification rate:", 1 - np.abs(T - np.round(Y)).sum() / N)