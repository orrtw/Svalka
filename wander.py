# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#%matplotlibnotebooself_value

t=0.87

def self_value(p,t):
    a=np.asarray([[0, 0, 1/p], 
                  [1, 0, -3/p], 
                  [0, 1, (8*t+p)/(3*p)]])
    l, w = np.linalg.eig(a)
    return l

def roots(p,t):
    a=np.asarray([[0, -1/p], 
                  [1, 2*(8*t+p)/(9*p)]])
    l, w = np.linalg.eig(a)
    return l

print(roots(0,t))

def p(v, t):
    return -3/v**2 +((8/3)*t)/(v-1/3)  

def trapezoid(f, v1, v2, n):
    h = (v2 - v1)/n
    result = 0.5*(f(v1,t) + f(v2,t))
    for i in range(1, n):
        result += f(v1 + i*h,t)
    result *= h
    return result

print(trapezoid(p, self_value(0.4,t)[0], self_value(0.4,t)[2], 1000))

v = np.linspace(0.5, 5, 100)
plt.plot(v, p(v,t)) 
plt.grid()
plt.show()

def dichotomia(f, v1, v2, eps, n):
   p_min = p(v1, t)
   p_max = p(v2,t)
   p0 = (p_min+p_max)/2
   i = trapezoid(f, v1, v2, n)
   while np.abs(p_min-p_max)/2 > eps:
        p0 = (p_min+p_max)/2
        if (i - (self_value(p0,t)[2]-self_value(p0,t)[0])*p0) == 0:
            return p0
        elif (i - (self_value(p0,t)[2]-self_value(p0,t)[0])*p0)>0:
           p_min,p_max = (p_min, p_max) 
        else:
           p_min,p_max = (p0,p_max)
        p0 = (p_min+p_max)/2
   return p0

print(dichotomia(p, 0.5, 1.8, 1e-5, 1000))
