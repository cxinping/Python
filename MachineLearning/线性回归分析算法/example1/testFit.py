# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:27:59 2017

@author: si
"""

import numpy as np

def fitSLR(x, y):
    n = len(x)
    dinominator = 0
    numerator = 0
    for i in range(0, n):
        numerator += (x[i] - np.mean(x))*(y[i] - np.mean(y))
        dinominator += (x[i] - np.mean(x))**2
    b1 = numerator/float(dinominator)
    b0 = np.mean(y)/float(np.mean(x))
    return b0, b1

def predict(x, b0, b1):
    return b0 + x*b1

x = [208,	152,	113,	227,	137,	238,	178,	104,	191,	130]
y = [21.6,	15.5,	10.4,	31.0,	13.0,	32.4,	19.0,	10.4,	19.0,	11.8]

b0, b1 = fitSLR(x, y)

print(  "intercept:", b0, " slope:", b1 )