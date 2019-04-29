#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:59:51 2019

@author: someone
Tracking of mobile in wireless network
"""

from numpy import dot,arange
from pylab import plot,xlabel,ylabel,show,title,legend

from numpy import loadtxt
#from pylab import plot,xlabel,ylabel,show,title,legend
def kf_predict(X, P, A, Q, B, U):
    X = dot(A, X) + dot(B, U)
    P = dot(A, dot(P, A.T)) + Q
    return(X,P)
    
from numpy import dot, sum, tile, linalg
from numpy.linalg import inv, det

def kf_update(X, P, Y, H, R): 
    IM = dot(H, X)
    IS = R + dot(H, dot(P, H.T)) 
    K = dot(P, dot(H.T, inv(IS))) 
    X = X + dot(K, (Y-IM))
    P = P - dot(K, dot(IS, K.T)) 
    LH = gauss_pdf(Y, IM, IS) 
    return (X,P,K,IM,IS,LH)

def gauss_pdf(X, M, S): 
    if M.shape[1] == 1:
        DX = X - tile(M, X.shape[1])
        E = 0.5 * sum(DX * (dot(inv(S), DX)), axis=0)
        E = E + 0.5 * M.shape[0] * log(2 * pi) + 0.5 * log(det(S)) 
        P = exp(-E)
    elif X.shape[1] == 1:
        DX = tile(X, M.shape[1])- M
        E = 0.5 * sum(DX * (dot(inv(S), DX)), axis=0)
        E = E + 0.5 * M.shape[0] * log(2 * pi) + 0.5 * log(det(S)) 
        P = exp(-E)
    else:
        DX = X-M
        E = 0.5 * dot(DX.T, dot(inv(S), DX))
        E = E + 0.5 * M.shape[0] * log(2 * pi) + 0.5 * log(det(S)) 
        P = exp(-E)
    return (P[0],E[0])
 
 
 # [topleftX, topleftY, bottomRightX, bottomRightY] or [NaN,NaN,NaN,NaN] 
 # if the object is not present in the frame
values = loadtxt("gt.txt",float,delimiter = ',')

x = (values[:,2]+values[:,0])/2
y = (values[:,3]+values[:,1])/2


#print(len(y))



#plot(x,y)
#show()







from numpy import *
from numpy.linalg import inv

#time step of mobile movement
dt = 0.1
# Initialization of state matrices
X = array([x[0], y[0], (x[1]-x[0])/dt, (y[1]-y[0])/dt]) # [x,y;dx/dt,dy/dt]
P = diag((0.01, 0.01, 0.01, 0.01))
A = array([[1, 0, dt , 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0,1]])
Q = eye(X.shape[0])
B = eye(X.shape[0])
U = zeros((X.shape[0],1))

from random import random
# Measurement matrices
Y = array([[x[0] + random()], [y[0] +random()]])
H = array([[1, 0, 0, 0], [0, 1, 0, 0]])
R = eye(Y.shape[0])
# Number of iterations in Kalman Filter
N_iter = 50
t_points = arange(0,50*dt,N_iter)

x_points = []   # estimated
y_points = []
x2_points = []  # measured
y2_points = []

# Applying the Kalman Filter
for i in range(len(x)//10):
    
    
    (X, P) = kf_predict(X, P, A, Q, B, U)
    (X, P, K, IM, IS, LH) = kf_update(X, P, Y, H, R)
    Y = array([[x[i] + abs(5 * random())],[y[i] +abs(5 * random())]])
    x_points.append(X[0,0])
    y_points.append(X[1,0])
    x2_points.append(Y[0,0])
    y2_points.append(Y[1,0])
    

    
plot(x_points,y_points,label = 'Estimated')
plot(x2_points,y2_points,'--', label = 'Measured')
legend()
show()
