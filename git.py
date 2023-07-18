#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:37:52 2023

@author: antoniosvasilatos
"""

import os
import numpy as np
import pandas as pd



#Convert dataframe from wide to long format
df = pd.read_excel(file_path)
df=pd.wide_to_long(df, ['GDP'], i=['COUNTRY'], j='Year', sep='')
df=df.reset_index()



#Filter dataset by country
specific_countries1 = ['Austria','Belgium', 'Denmark','Finland','France','Germany','Greece','Ireland','Italy','Netherlands','Norway','Portugal','Spain','Sweeden','Switzerland','United Kingdom']


df = df[df['COUNTRY'].isin(specific_countries1)].sort_values(by='COUNTRY')



# Merge the two dataframes based on 'year' and 'country'
merged_df = df1.merge(df, on=['Year', 'COUNTRY'], how='left')

