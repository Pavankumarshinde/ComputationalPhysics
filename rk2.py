# -*- coding: utf-8 -*-
"""

"""
import math
import numpy as np
import matplotlib.pyplot as plt

def deriv(farr,x):
    deriv_arr=np.array([farr[2],farr[3],np.sin(farr[1]),np.cos(farr[0])])    
    return(deriv_arr)

f0arr=np.array([0,0,0,0])
dt=1E-4
T=50.0
N=int(T/dt)

fsol=[]
fsol.append(f0arr)

time=0.0
for i in range (0,N):
    k1 = dt*deriv(f0arr,time)
    k2 = dt*deriv(f0arr+0.5*k1,time+0.5*dt)
    f1arr = f0arr+k2
    time  = time+dt
    fsol.append(f1arr)
    f0arr = f1arr

fsolution = np.array(fsol)

plt.plot(fsolution[:,0], fsolution[:,1])
plt.show()




