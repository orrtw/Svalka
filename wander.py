# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import numpy as np
import matplotlib.pyplot as plt

t=0.9
def k(p):
    a=np.asarray([[0, 0, -1/p], 
                  [1, 0, -3/p], 
                  [0, 1, 1/(3*p)*(1+8*t)]])
    l, w = np.linalg.eig(a)
    return l
print(k(0.2))
    
def p(v, t):
    return (-3/v**2 +(8*t/3)/(v-1/3))   
v = np.linspace(0.2, 1, 100)

plt.plot(v, p(v,t)) 
plt.show()