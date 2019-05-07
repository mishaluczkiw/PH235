#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 02:32:00 2019

@author: Misha Luczkiw

Kalman filtering on financial stock market data
"""

from numpy import random,  zeros,loadtxt
from math import sin
from numpy.random import normal
import matplotlib.pyplot as plt
from pylab import plot, title, legend, xlabel, ylabel,title,show

x = loadtxt('dow2.txt',float)


# intial parameters
n_iter = len(x)
sz = (n_iter) # size of array
#x = -0.37727 # truth value (typo in example at top of p. 13 calls this z)
#z = normal(x,0.1,size=sz) # observations (normal about x, sigma=0.1)
z = x
Q = 1e-5 # process variance

# allocate space for arrays
xhat=zeros(sz)      # a posteri estimate of x
x_avg = zeros(sz)
P=zeros(sz)      # a posteri error estimate
xhatminus=zeros(sz) # a priori estimate of x
Pminus=zeros(sz)    # a priori error estimate
K=zeros(sz)         # gain or blending factor

R = 0.1**2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = 10000.0
P[0] = 1.0

for k in range(1,n_iter):
    # time update
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1]+Q

    # measurement update
    K[k] = Pminus[k]/( Pminus[k]+R )
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
    P[k] = (1-K[k])*Pminus[k]

# compute running average extimate
samples = 100
for k in range(1,n_iter):
    if k < samples:
        x_avg[k] = sum(z[0:k])/len(z[0:k])
    else:
        x_avg[k] = sum(z[k-samples:k])/len(z[k-samples:k])

        
    

plot(z,'k+',label='noisy measurements')
plot(xhat,'b-',label='a posteri estimate')
#plot(x_avg,'r',label='running average with length')
legend()
title('Estimate vs. iteration step', fontweight='bold')
xlabel('Days')
ylabel('Dow Jones Market Value')
show()

