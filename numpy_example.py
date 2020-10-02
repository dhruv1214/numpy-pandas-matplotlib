# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:01:46 2020

@author: 66IN
"""


import numpy as np
import sys

'''
a = np.array([(1,2,3),(4,5,6)])

print((a)) 




s = range(1000)
print(sys.getsizeof(5)*len(s))

d = np.arange(1000)
print(d.size*d.itemsize)

'''

a = np.array([1,4,2,3,5,7,8,6])
x = a.reshape(4, 2) 
print(x)
print()
y = x.reshape(2, 4)
print(y)

a = np.array([1,4,2,3,5,7,8,6])
x = a.reshape(2, 4)
print(x)
y = x.flatten() 
print(y)
