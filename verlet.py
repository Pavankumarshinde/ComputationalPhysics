# -*- coding: utf-8 -*-
"""
Implementing Verlet method for solving
equation of motion of particle in a given
force field
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#defining acceleration field
def accel(xarr,t):
    a_vec = np.array([np.sin(xarr[1]),np.cos(xarr[0])])
    #r=np.sqrt(xarr[0]**2+xarr[1]**2)
    #a_vec = np.array([-xarr[0]/r**3,-xarr[1]/r**3]) 
    return a_vec


#set time T and dt
endT  = 50
dt = 0.000001

#define intial position and velocity
x0_arr=np.array([0,0])
v0_arr=np.array([0,0])

#create a list to store the solution
xsol_arr=[]
xsol_arr.append(x0_arr) #append the initial position 


a0_arr=accel(x0_arr,0) #initial acceleration
#calcuate x-, the position at previous step
x_prev=x0_arr-dt*v0_arr+(dt**2/2.0)*a0_arr


time=0.0
while(time <= endT):
    x_next = -x_prev+2*x0_arr+(dt**2)*accel(x0_arr,time)
    xsol_arr.append(x_next)
    x_prev = x0_arr
    x0_arr = x_next    
    time += dt
    print(time)
    
    
xsolution=np.array(xsol_arr)
#print((xsolution))    


plt.plot(xsolution[:,0], xsolution[:,1])
plt.show()