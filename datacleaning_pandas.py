#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:31:26 2021

@author: anil
"""
import numpy as np
import pandas as pd
from numpy import nan
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})
'''
1. Some values in the the FlightNumber column are missing. These numbers are
meant to increase by 10 with each row so 10055 and 10075 need to be put in
place. Fill in these missing numbers and make the column an integer column
(instead of a float column).
'''
'''
2. The From_To column would be better as two separate columns! Split each
string on the underscore delimiter _ to give a new temporary DataFrame with
the correct values. Assign the correct column names to this temporary
DataFrame.
'''
for k in range(len(df)):
    #print(k)
    check_for_nan = df['FlightNumber'].isnull()
    if check_for_nan[k] == True: 
        print(df['FlightNumber'][k])
        df['FlightNumber'][k] = g+10
    else:
        g = df['FlightNumber'][k]
        
'''
 3. Notice how the capitalisation of the city names is all mixed up in this
temporary DataFrame. Standardise the strings so that only the first letter is
uppercase (e.g. "londON" should become "London".)
'''      
df["from"] = 0
df["to"] = 0
for k in range(len(df)):
    txt=df["From_To"][k]
    x = txt.split("_")
    df["from"][k] = x[0]
    df["to"][k] = x[1]       
'''
4. Delete the From_To column from df and attach the temporary DataFrame
from the previous questions.
'''
      
for k in range(len(df)):    
    df["from"][k] = df["from"][k].lower() 
    df["to"][k] = df["to"][k].lower()
    u = df["from"][k][0].upper()
    o = df["from"][k][1::]
#print(o)
    j = u+o
    print(j)
    df["from"][k] = j
    uu = df["to"][k][0].upper()
    oo = df["to"][k][1::]
#print(o)
    jj = uu+oo
    print(jj)
    df["to"][k] = jj
'''
5. In the RecentDelays column, the values have been entered into the
DataFrame as a list. We would like each first value in its own column, each

second value in its own column, and so on. If there isn't an Nth value, the value
should be NaN.
'''    
for k in range(len(df)):    
    if df["RecentDelays"][k] == []:
       df["RecentDelays"][k] = "nan"
    
    
    
    
    
    
    
    
    
    
   