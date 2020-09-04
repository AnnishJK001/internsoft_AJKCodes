#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('NVDA.csv',usecols= [ 1,2,3,4])  #imports only 1,2,3,4 columns

pohl_avg = data[['Price','Open','High','Low']].mean(axis= 1)
multi = data[['Price','Open']].sum(axis=1)
print(multi)
print(pohl_avg)   #calculating the average
 
fg = np.arange(1,len(data)+1,1) #print(fg)

plt.plot(fg,pohl_avg,multi,'r',label = 'plotting')



            

