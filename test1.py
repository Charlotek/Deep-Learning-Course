# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:08:23 2020

@author: zhaojf
"""

import numpy as num
a=int(input("(1-100)a="))
i=0
j=1
num.random.seed(612)
while i<1000:
    x=num.random.uniform(0,1)
    if i%a==0:
        print("%d\t%d\t%f\t"%(j,i,x))
        j=j+1
    i=i+1
5