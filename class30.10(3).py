# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:16:57 2018

@author: Наталия 
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats 

tau1= 0.4
tau2 = 0.6
mu1= np.array([0.5, 0.5])
mu2 = np.array([-0.5,-0.5])
sigma1 = 0.4
sigma2 = 0.3
n=1000

x_n1 = stats.multivariate_normal(mu1, sigma1**2).rvs(int(n * tau1))
x_n2 = stats.multivariate_normal(mu2, sigma2**2).rvs(int(n * tau2))
x_u = stats.uniform(np.array([-1.5, -1.5]), np.array([3.0, 3.0])).rvs(int(n*(1-tau1-tau2)))

x = np.vstack([x_n1, x_n2])

print(x)
#plt.plot(*x, '*', color='red')
plt.scatter(*x.T, color='red')


#stats.multivariate_normal(mu, sigma1**2, sigma2**2)
                          