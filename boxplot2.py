#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:42:38 2023

@author: deleryharrison
"""

#Purpose: Create box plot for period 2 data
#Name: Delery Harrison
#Date: 02/12/2023
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata2.csv")
df2.boxplot(); plt.suptitle('Period 2 box plot')
plt.show()
