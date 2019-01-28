# -*- coding: utf-8 -*-
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
#%matplotlibnotebook
t=0.88
def k(p):
    a=np.asarray([[0, 0, -1/p], 
                  [1, 0, -3/p], 
                  [0, 1, 1/(3*p)*(1+8*t)]])
    l, w = np.linalg.eig(a)
    return l
#print(k(0.2)[0])
    
def p(v, t):
    return -3/v**2 +((8/3)*t)/(v-1/3)   


def trapezoid (func,t, a,b,n):
    x = np.linspace(a,b,n)
    f = np.array(func(x,t))
    b = []
    for i in range (len(x)-1):
        f_integ = ((f[i]+f[i+1])*(x[i+1] - x[i]))/2
        b.append(f_integ)
    return (sum(np.array(b))) 
print(trapezoid(p, 0.88, 0.6, 1.5, 100))
v = np.linspace(0.5, 5, 100)
'''plt.plot(v, p(v,0.88)) 
plt.grid()
plt.show()
'''
a1=0.5
b1=1
def dichotomy:
    l =(a1+b1)/2
    