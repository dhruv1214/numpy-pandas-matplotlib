# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:38:15 2020

@author: 66IN
"""


import pandas as pd

import numpy as np


s = pd.Series([1,2,3,4,np.nan,5,6])   #using series in pandas


print(s)

# example of dataframe :


d = pd.date_range('20200301',periods=10)

print(d)

df = pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])

print(df)

df1 = pd.DataFrame({'A':[1,2,3,4],
                    
                    
                    'B':'Aditya'})

print(df1)


#functions in python

print(df.head())
print(df.tail())


print(df.to_numpy())