# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:25:48 2018

@author: Наталия 
"""
import numpy as np
import scipy as sp
from scipy import stats
from scipy.optimize import fmin_powell

def data_generation():
    mu1 = 0.5
    tau = 0.5 
    sigma1 = 0.3 
    mu2 = 0.6
    sigma2 = 0.1
    n = 100
    
    x_n1 = stats.norm.rvs(loc=mu1, scale=sigma1, size=int(tau*n))
    x_n2 = stats.norm.rvs(loc=mu2, scale=sigma2, size=int(tau*n))
    x = np.concatenate((x_n1, x_n2))
    return x

def max_likelihood(x, tau, mu1, sigma1, mu2, sigma2, xtol=1e-3):  
    f1 = stats.norm.pdf(x, loc = mu1, scale = sigma1) 
    f2 = stats.norm.pdf(x, loc = mu2, scale = sigma2) 
    f = f2 + f1

    m = fmin_powell(-f, x, args=(tau, mu1, sigma1, mu2, sigma2), xtol=1e-3, full_output=0, disp=1)
    return m
print(max_likelihood(data_generation(), 0.6, 0.1, 0.2, 0.3, 0.4, xtol=1e-3))



