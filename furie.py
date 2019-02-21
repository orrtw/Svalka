# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:13:54 2019

@author: student
"""

import numpy as np
import matplotlib as plt

n = inf
omega = 3

def f(t):
    return np.sin(omega*t)


def f_(f):
    for i in range (-n, n):
        f()
    return np.sum(f*np.exp(np.j*k*2*np.pi/t))





    
    
    
    
    
    
    