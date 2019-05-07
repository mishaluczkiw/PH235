#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 02:32:00 2019

@author: macbookair
"""

from numpy import random,  zeros
from math import sin,sqrt
from numpy.random import normal
import matplotlib.pyplot as plt
from pylab import plot, title, legend, xlabel, ylabel,title,show


# intial parameters
n_iter = 50
sz = (n_iter) # size of array
x = -0.5 # truth value (typo in example at top of p. 13 calls this z)
z = normal(x,0.1,size=sz) # observations (normal about x, sigma=0.1)

Q = 1e-5 # process variance

# allocate space for arrays
xhat=zeros(sz)      # a posteri estimate of x
x_avg = zeros(sz)
P=zeros(sz)      # a posteri error estimate
xhatminus=zeros(sz) # a priori estimate of x
Pminus=zeros(sz)    # a priori error estimate
K=zeros(sz)         # gain or blending factor

R = 0.01**2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = 0.0
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
samples = 10
for k in range(1,n_iter):
    if k < samples:
        x_avg[k] = sum(z[0:k])/len(z[0:k])
    else:
        x_avg[k] = sum(z[k-samples:k])/len(z[k-samples:k])

        
    

plot(z,'k+',label='noisy measurements variance = 0.1')
#plot(xhat,'b-',label='Kalman filter estimate variance = '+str(sqrt(R)))
#plot(x_avg,'r',label='running average length '+str(samples))
legend()
title('Estimate vs. iteration step', fontweight='bold')
xlabel('Iteration')
ylabel('Voltage')
show()

#plot(P[1:len(P)-1])
#title('Estimated a priori error vs iteration step')
#show()
