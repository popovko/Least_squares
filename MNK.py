import numpy as np
from numpy import linalg as la
import math
import matplotlib as mpl
from matplotlib import pyplot as plt
import pylab



def func(x):
    return x

def inputPoints():   
    n = int(input('Count points: '))
    print('Input points (xi yi in lane) \n')
    D = np.zeros((n ,2))
    for i in range(n):
        point = input()
        D[i][0] = float(point.split(' ')[0])
        D[i][1] = float(point.split(' ')[1])
    plt.scatter(D[:,0], D[:,1], color = 'green')
    return D

def calcCoef():
    D = inputPoints()
    M = D.shape[0]
    power = int(input('Input power polinom: '))
    A = np.zeros((M, power+1))
    A[:, 0] = np.ones(M)

    for i in np.arange(power)+1:
        A[:, i] = func(D[:, 0])**i

    W = np.dot(la.inv(np.dot(A.transpose(), A)), np.dot(A.transpose(), D[:, 1]))
    W = np.around(W, decimals=3)
    
    x = np.arange(np.amin(D[:, 0] - 5), np.amax(D[:, 0] + 5), 0.25)
    y = np.zeros(x.shape)

    print(W)

    for i in range(power + 1):
        y += W[i] * (np.power(x, i))
    #print(x)
    #print(y)
    pylab.plot(x, y)
    pylab.show()

calcCoef()