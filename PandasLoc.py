# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:45:28 2020

@author: gmunaretti
"""

# importing pandas as pd 
import pandas as pd 
  
# Creating the DataFrame 
df = pd.DataFrame({"A":[12, 4, 5, None, 1],  
                   "B":[7, 2, 54, 3, None],  
                   "C":[20, 16, 11, 3, 8],  
                   "D":[14, 3, None, 2, 6]})  
  
# Create the index 
index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5'] 
  
# Set the index 
df.index = index_ 
  
# Print the DataFrame 
print(df) 



# return the values. 
result = df.loc[:, ['A', 'D']] 
  
# Print the result 
print(result)



################################################