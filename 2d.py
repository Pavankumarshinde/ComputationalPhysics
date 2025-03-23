# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:40:13 2025

@author: Kirit
"""

import numpy as np


def simpson(farr,Dx):
    l = np.size(farr)
    it = 0.0
    for i in range(0,l-2,2):
        it += (Dx/3.0)*(farr[i]+4*farr[i+1]+farr[i+2])
    return it
       
def func(x,y):
    return np.exp(-x**2-y**2)

def main():
    N=80
    
    garr = np.zeros(N+1)
    farr = np.zeros(N+1)
    xarr = np.linspace(-1,1,N+1)
    
    for i in range (0,N+1):
        if (i==0 or i==N):
            garr[i]=0
        else:
            xval = xarr[i]
            ymin = -np.sqrt(1-xval**2)
            ymax = -ymin
            yarr = np.linspace(ymin,ymax,N+1)
            for j in range (0,N+1):
                yval = yarr[j]
                farr[j]=func(xval,yval)
            garr[i]=simpson(farr,(ymax-ymin)/N)
            
    integral = simpson(garr,2.0/N)
    
    print(integral)


if __name__ == '__main__':
    main()


    

