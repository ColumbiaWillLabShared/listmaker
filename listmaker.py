# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:42:56 2019

@author: Columbia
"""

import numpy as np

start = 6.5
stop = 8
step = 0.1
listx = np.round(np.arange(start,stop+step,step),2)

for x in listx:
    print (x)