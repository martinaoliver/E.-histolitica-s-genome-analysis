# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 17:32:00 2017

@author: Martina Oliver
"""
import pandas as pd

#Importing dataframes and values

dataframe = pd.read_csv('C:/Users/Martina Oliver/Dropbox/HUNTLEY/Ehist_EST.txt',  delim_whitespace=True, header= None)

titles = pd.read_csv('C:/Users/Martina Oliver/Dropbox/HUNTLEY/BLAST_columns_1.txt', header= None)

dataframe.columns = titles.values.flat


#data_filtered = dataframe[dataframe['Percent identity']>95.0]


print(data_filtered)
#print dataframe

data_filtered.to_csv("filtered_hist_data")


print data_filtered

