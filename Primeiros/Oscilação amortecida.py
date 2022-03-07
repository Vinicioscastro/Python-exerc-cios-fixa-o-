# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:43:18 2018

@author: linhars
"""

from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style 
import math

#-------------=====================Runge-Kutta--------------------------- 


def f(y,v): #y=p
    return -1-4*k*k*y*y-4*k*k*y*v*v+y*(2*g1*k-w*w)

def g(y,v):
    return v

c=5.0
m=1
k=0.10
g1=9.8
w=15
#n=100
n=100
t0=0

v0 = 4.0
y0 =1.0
#h =(tf-t0)/n
dt=0.01

t=[t0]
v=[v0]
y=[y0]

for i in range(n):
    k1 = f(y0,v0)
    L1 = g(y0,v0)
    k2 = f(y0+dt/2*L1,v0+dt/2*k1)
    L2 = g(y0,v0+dt/2*k1)
    k3 = f(y0+dt/2*L2,v0+dt/2*k2)
    L3 = g(y0,v0+dt/2*k2)
    k4 = f(y0+dt*L3,v0+dt*k3)
    L4 = g(y0,v0+dt*k3)
   
    y0 = y0+dt/6*(L1+2*L2+2*L3+L4)
    y.append(y0)
    v0 = v0+dt/6*(k1+2*k2+2*k3+k4)
    t0=t0+dt
    t.append(t0)

print(y)
   

plt.plot(t,y,'bo-')
  
plt.xlabel('Tempo',fontsize=13)
plt.ylabel('Posicao',fontsize=13)

#plt.savefig("aro.jpg")
plt.show()    
 
