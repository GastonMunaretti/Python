# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:48:38 2020

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


# find mod of dataframe values with 3 
df.mod(3) 