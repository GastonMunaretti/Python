# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:56:37 2020

@author: gmunaretti
"""

# importing pandas as pd 
import pandas as pd 
  
# Creating the dataframe  
df = pd.DataFrame({"A":[12, 4, 5, 44, 1],  
                   "B":[5, 2, 54, 3, 2],  
                   "C":[20, 16, 7, 3, 8],  
                   "D":[14, 3, 17, 2, 6]}) 
  
# Print the dataframe 
df 


# create a seires 
sr = pd.Series([3, 2, 4, 5]) 
  
# setting its column index similar to the dataframe 
sr.index =["A", "B", "C", "D"] 
  
# print the series 
sr 

# find mod of dataframe values with series 
# axis = 1 indicates column axis 
df.mod(sr, axis = 1) 