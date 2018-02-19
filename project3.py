# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:15:52 2017

@author: Martina Oliver
"""
import pandas as pd
sequences = pd.read_csv('C:/Users/Martina Oliver/Dropbox/HUNTLEY/filtered_data_project2.txt' , header= None)
miRNA = pd.read_csv('C:/Users/Martina Oliver/Dropbox/HUNTLEY/palindrome_seqs.txt',  delim_whitespace=True, header= None)

header = sequences.iloc[0]
sequences = sequences [1:]
sequences.columns = header.values.flat

miRNA.columns = ['SEQUENCE']
miRNA ['SEQUENCE ID']= miRNA['SEQUENCE'].map(lambda x: x.rstrip('ATGC').lstrip ('>'))

s=0
m=0
array = []
for s in range (0,124):
	for m in range (0,67):
		if (miRNA.iloc[s,1]) == (sequences.iloc[m,1]):
			array.append(miRNA.iloc[s,1])
		m+=1
	s+=1
	
expressed_microRNA = map(( lambda x: '>' + x), array)
df = pd.DataFrame(expressed_microRNA)
df.columns = ['EXPRESSED_microRNA']
df.to_csv('Final_EXPRESSED.microRNA')


print s
