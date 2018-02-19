# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:51:27 2017

@author: Martina Oliver
"""
import pandas as pd

sequences = pd.read_csv('C:/Users/Martina Oliver/Dropbox/HUNTLEY/filtered_data_project2.txt' , header= None)

#put headers to dataframe
header = sequences.iloc[0]
sequences = sequences [1:]
sequences.columns = header.values.flat
sequences1 = sequences.drop([2])
x=0 
d = {}

#create a dictionary where its shown how many subject labels are repeated and how many times. 
for x in range (0,66):

	if sequences1.iloc[x,2] in d:  
		d[sequences1.iloc[x,2]]+=1
	else: 
		d[sequences1.iloc[x,2]] =1
		
	x+=1
	


y=0

for y in range (0,66):
	if d[sequences1.iloc[y,2]] == 1:
		del d[sequences1.iloc[y,2]] 
		


#when two subject[EST] are the same, delete the row with the lowest percent identity. In this case one EST is matched by more than one SINE. This happens because SINES are very similar so therefore a SINE that hasnt been expressed can match an EST from another SINE. This other SINE is very similar to the first SINE but we want to delete the first SINE as is not the real one that was expressed. compare % 
x1=1
y1=1
for x1 in range (1,66):
	if sequences1.iloc[x1,2] in d:
		a1 = sequences1.iloc[x1,2] 
		for y1 in range (1,66):
			if a1 == sequences1.iloc[y1,2]:
				if (sequences1.iloc[x1,3]) < (sequences1.iloc[y1,3]):
					sequences1.drop([x1])
					print sequences1.iloc[y1]
				if (sequences1.iloc[x1,3]) > (sequences1.iloc[y1,3]):
					sequences1.drop([y1])
					print sequences1.iloc[x1]
				else: print False

#if (sequences1.iloc[10,3]) < (sequences1.iloc[11,3]):
#	a2 = sequences1.drop([1])
#	print sequences1.iloc[11,3]
#else: 
#	a2 = 1
r6
	