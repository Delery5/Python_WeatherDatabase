#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:55:25 2023

@author: deleryharrison
"""

#Purpose: Create a histogram of humidity data from the second period
#Name: Delery Harrison
#Date: 02/12/2023
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
df2['Humidity'].hist(bins=10, alpha=0.5); plt.suptitle('Histogram of Humidity')
plt.show()
