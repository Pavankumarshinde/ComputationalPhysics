# -*- coding: utf-8 -*-
"""
2D poisson equation solving with Jacobi method
"""

import numpy as np
import matplotlib.pyplot as plt

#define the potential matrix
N  = 100
M  = 100
l2 = 1.0
eps = 0.0001

V0=np.zeros([M+2,N+2])
V1=np.zeros([M+2,N+2])
dx = 1.0/(N+2)
dy = 1.0/(M+2)

#apply boundary condition
#lets take first index as y axis and second index as x axis
V0[:,0]=1.0*np.sin(2*np.pi*np.linspace(0,1,M+2))
V1[:,0]=1.0*np.sin(2*np.pi*np.linspace(0,1,M+2))

step = 0
while (l2 > eps):

    #for i in range(1,M+1):
    #    for j in range(1,N+1):
    #        V1[i,j]=0.25*(V1[i+1,j]+V1[i-1,j]+V1[i,j+1]+V1[i,j-1])


    V1[1:M+1,1:N+1]=0.25*(V0[0:M,1:N+1]+V0[2:M+2,1:N+1]+V0[1:M+1,0:N]+V0[1:M+1,2:N+2])
    l2 = np.sqrt(np.sum((V1-V0)**2))
    V0 = np.copy(V1)
    print("step= ", step, "l2 = ", l2)
    step += 1
    
    
c = plt.imshow(V1, cmap ='jet',
                    interpolation ='nearest', origin ='lower') 
plt.colorbar(c)
plt.show()
    
    
    



