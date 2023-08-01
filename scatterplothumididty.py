#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:00:41 2023

@author: deleryharrison
"""

#Purpose: Create scatter plot of humidity for period 1. Can replace df1 to df2 to display second period data
#Name: Your name
#Date: Your date
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
plt.scatter(df1.index.values,df1['Humidity']); plt.suptitle('Humidity')
plt.show()
