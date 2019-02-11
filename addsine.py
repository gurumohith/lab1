#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:09:20 2019

@author: aravind
"""

import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()      #creating subplots
plt.subplots_adjust(left=0.125,right=0.9,bottom=0.1,top=0.9,wspace=0.5,hspace=0.8)#adjusting size of the subplots
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
n=np.linspace(0,10,1000)
x1=np.sin(2*np.pi*2000*n)
y1=np.sin(2*np.pi*2000*n)
z1=x1+y1
ax1.plot(n,z1)
ax1.set_title("when f1=f2")
ax1.set_xlabel("----------->time")
ax1.set_ylabel("amplitude")
x2=np.sin(2*np.pi*1000*n)
y2=np.sin(2*np.pi*2000*n)
z2=x2+y2
ax2.plot(n,z2)
ax2.set_title("when f1 is not equal to f2")
ax2.set_xlabel("----------->time")
ax2.set_ylabel("amplitude")

