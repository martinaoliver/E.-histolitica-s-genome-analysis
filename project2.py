# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:44:16 2017

@author: Martina Oliver
"""

import pandas as pd

blast = pd.read_csv('C:/Users/Martina Oliver/Dropbox/HUNTLEY/Ehist_EST.txt',  delim_whitespace=True, header= None)
sines = pd.read_excel('C:/Users/Martina Oliver/Dropbox/HUNTLEY/SINE_Positions.xls', header= None)
#import both archivos
titles = pd.read_csv('C:/Users/Martina Oliver/Dropbox/HUNTLEY/BLAST_columns_1.txt', header= None)
#titles2 = pd.read_csv('C:/Users/Martina Oliver/Dropbox/HUNTLEY/columns.sines.txt' , sep = '          ' , header=None)
blast.columns = titles.values.flat
header = sines.iloc[0]
sines = sines[1:]
sines.columns = header.values.flat


#put header to blast and sines

blast['ID1'] = blast['Query label'].apply(lambda x: x.split ('_')[0])

#clear first column which results in a ID number (remove extra letters)- to obtain key
df = blast[blast['Percent identity']>95.0]
#filter those with high % identity





yd=0
ys=0

lenght_array=[]
for yd in range (0,87): 
	for ys in range (0,393):
		if int(df.iloc[yd,12]) == int(sines.iloc[ys,0]):
			lenght_array.append(sines.iloc[ys,5])
			
		ys+=1
	yd+=1


df.insert(13,'SINES LENGHT', lenght_array)

		

#obtaining SINE lenght from the SINES that matched in the blast search. Put into an array
# The 393 is because the two last ones are NaN. 		



#df1 = df.assign('ALIGNMENT LENGHT'= df['End position in query'] - df['Start position in query'])
##find alignment lenght
#df2 = df1.assign('COVERAGE'=df1['SINE START'] / df1['SINES LENGHT'])
df['ALIGNMENT LENGHT'] = df['End position in query']-df['Start position in query']
df['COVERAGE']=df['ALIGNMENT LENGHT']/df['SINES LENGHT']
DATA = df[df['COVERAGE']>0.95]
print DATA

DATA.to_csv('filtered_data_project2')
#print jordi
#filter those whose alignment covers more than 95% of the sequence
#print df3['SINE length (bp)']
#print blast['ID2']

print df.iloc[1,12]

