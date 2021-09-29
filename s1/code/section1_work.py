#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:20:41 2021

@author: bdobkowski
"""
import numpy as np
from scipy.optimize import minimize
import scipy.integrate as integrate
from matplotlib import pyplot as plt

# 1. define a sine function using numpy
def myFcn(t):
    return np.sin(t)

# 2. find minimum of the function using scipy
x0 = np.array([-0.5])
minimum = minimize(myFcn, x0)
print('Minimum:')
print(minimum)

# 3. integrate the function from 0 to 1 using scipy
integral, err = integrate.quad(myFcn, 0, 1)
print('Integral:')
print(integral)

# 4. plot the function using Matplotlib from [0, 2pi]
t = np.arange(0, 2*np.pi, 0.001)
fig, ax = plt.subplots()
ax.plot(t,myFcn(t))
ax.set_title('sin(t) over [0, 2*pi]')
ax.set_xlabel('t')
ax.set_ylabel('sin(t)')
fig.savefig('my_sin_fig')
