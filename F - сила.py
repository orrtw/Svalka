# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:42:53 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 10000

#N1 = np.random.uniform(0,n)

mu, sigma = 40, 0.05
mu1 , sigma1 = 30, 0.1
mu2, sigma2 = 3.2, 0.01


M = np.random.normal(mu, sigma, n)
M1 = np.random.normal(mu1, sigma1, n)
r = np.random.normal(mu2, sigma2, n)
G = 6.67384*1e-3

def F(m, m1, r):
    return G*m*m1/r**2

f = F(M, M1, r)
#print (f)

mur, std = norm.fit(f)

#plt.hist(f, bins=20, density=True, alpha=0.6, color='g')
#
#xmin, xmax = plt.xlim()
#x = np.linspace(xmin, xmax, 100)
#p = norm.pdf(x, mu, std)
#plt.plot(x, p, 'k', linewidth=2)
#plt.hist(f)
#plt.show()
print('mu', mur, 'sigma', std)
m = 40
m1 = 30
r = 3.2
F = m*m1*G/r**2

s1 = (sigma/m)**2
s2 = (sigma1/m1)**2
s3 = 4*(sigma2/r)**2
sigmaa = np.mean(np.sqrt(F*(s1+s2+s3)))

print(sigmaa)


    
    