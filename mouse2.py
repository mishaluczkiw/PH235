#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 01:44:06 2019

@author: Misha Luczkiw
Displays mouse position plus noise
Kalman filtering gives predicted position
"""
from cs1lib import *
from random import uniform, random
from numpy import array, dot, diag,eye,empty
from numpy.linalg import inv


def press(mx, my):
    global draw
    draw = True

def release(mx, my):
    global draw
    draw = True#False

def move(mx, my):
    global  x, y

    x = mx
    y = my

def graphics():
    global P, last_x
    #print(x)
    clear()
    if draw:
        # true position
        #set_fill_color(r, g, b)
        #draw_circle(x, y, 4)
        
        # noisy measurement
        
        cur_xPos = x+100*(random()-0.5)
        cur_yPos = y+100*(random()-0.5)
        
        set_fill_color(1, 0, 0) # red
        draw_circle(cur_xPos,cur_yPos,1)
        
        
        
        # Kalman filtered point
        
        new_x,new_P = kf_predict(cur_xPos, cur_yPos, last_x)
        last_x[0] = new_x[0]
        last_x[1] = new_x[1]
        P = new_P
        
        set_fill_color(0, 1, 0) # green
        draw_circle(new_x[0],new_x[1],4)
        
        # prediction
        draw_line(new_x[0],new_x[1],cur_xPos,cur_yPos)


def kf_predict(cur_xPos, cur_yPos, last_x):
    global P
    dt = 0.2
    A = array([
		[1, 0, dt, 0],
		[0, 1, 0, dt],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	])
    
    B = array([
    		[1, 0, 0, 0],
    		[0, 1, 0, 0],
    		[0, 0, 1, 0],
    		[0, 0, 0, 1]
    	])
        
    H = array([
    		[1, 0, 1, 0],
    		[0, 1, 0, 1],
    		[0, 0, 0, 0],
    		[0, 0, 0, 0]
    	])
    
    Q = array([
    		[0, 0, 0, 0],
    		[0, 0, 0, 0],
    		[0, 0, 0.1, 0],
    		[0, 0, 0, 0.1]
    	])
    
    R = array([
    		[0.1, 0, 0, 0],
    		[0, 0.1, 0, 0],
    		[0, 0, 0.1, 0],
    		[0, 0, 0, 0.1]
    	])
    
    
    velX = cur_xPos - last_x[0]
    velY = cur_yPos - last_x[1]
    measurement = array([cur_xPos, cur_yPos, velX, velY])
    control = array([0,0,0,0])
    
    #prediction
    x = dot(A,last_x) + dot(B,control)
    P = dot(A, dot(P, A.T)) + Q
    
    
    # correction
    S = R + dot(H, dot(P, H.T))
    K = dot(P, dot(H.T, inv(S)))
    y = measurement-dot(H,x)
    
    cur_x = x+dot(K,y)
    cur_P = dot(eye(4)-dot(K,H),P)
    
    last_x = cur_x
    last_P = cur_P
    return (last_x,last_P)

    
    
    
r = 0
g = 1
b = 0
x = 0
y = 0
draw = True




global P
global last_x
P = empty([4,4],float)
last_x = array([0.0,0.0,0.0,0.0])

start_graphics(graphics, 2400, mouse_move=move, mouse_press=press)


