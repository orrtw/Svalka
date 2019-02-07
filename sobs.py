# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:13:54 2019

@author: student
"""

import numpy as np
import matplotlib as plt
n = 10

a = 5
h = 6,62*10**(-34)
m = 9*10**(-31) 

p = 1/n

l = np.linspace(-a, a, n)
def matr(n):
    A = np.zeros((n,n))
    for i in range (n):
        for j in range(n):
            if i == j:
                A[i, j] = -2
            if j == i-1:
                A[i,j] = 1
            if j == i +1:
                A[i,j] = 1
    return A

print(matr(n))

k = np.linalg.eig(matr(n))[0]

print(np.linalg.eig(matr(n))[0])


 
def energ(k):
    e = (h*k)**2/(2*m*p**2)
    return e 

e_n = np.array([energ(k)[i]] for i in range (len(k))

plt.plot()





    
    
    
    
    
    
    