  # -*- coding: utf-8 -*-
"""

"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

def p_func(x):
    return np.sin(x)

def q_func(x):
    return 1.0+0.0*x

def s_func(x):
    return 0.0+0.0*x

#define number of internal points
N=100
a=0
b=4.0*np.pi

#boundary condition
fa = 0.0
fb = 1.0

dx = (b-a)/(N+1)

print(dx)

#define the x grid array
xgrid = np.linspace(a,b,num=N+2)

p_arr = p_func(xgrid)
q_arr = q_func(xgrid)
s_arr = s_func(xgrid)

#create D, S, and B matrices
S_mat = s_arr[1:N+1]

B_mat = np.zeros(N)
B_mat[0] = ((1/dx**2)-p_arr[1]/(2*dx))*fa
B_mat[-1] = ((1/dx**2)+p_arr[N]/(2*dx))*fb 

D_mat = np.zeros([N,N])

for i in range(0,N):
    D_mat[i,i] = q_arr[i+1]-(2/dx**2)
    if (i<N-1):
        D_mat[i,i+1] = (1/dx**2) + p_arr[i+1]/(2*dx)
    if (i>0):
        D_mat[i,i-1] = (1/dx**2) -p_arr[i+1]/(2*dx)
    
print(D_mat)


Dinv = inv(D_mat)

F_mat = np.matmul(Dinv,(S_mat-B_mat))

print(F_mat)

f_arr = np.zeros(N+2)
f_arr[0] = fa
f_arr[1:N+1] = F_mat
f_arr[N+1] = fb

plt.plot(xgrid, f_arr)
plt.show()



