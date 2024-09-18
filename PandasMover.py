# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:17:53 2020

@author: gmunaretti
"""

# importing pandas module   
import pandas as pd  
  
# reading csv file from url   
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  
  
# creating column and row variables 
column = 7
row = 3
      
# calling .iat[] method 
output = data.iat[row, column] 
  
# display 
print(output) 
  
# df display 
data.head() 