# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:59:17 2020

@author: gmunaretti
"""
# importing pandas module  
import pandas as pd 
  
# reading csv file from url  
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
   
# dropping null value columns to avoid errors 
data.dropna(inplace = True) 

# creating new column for len 
# passing values through str.len() 
data["Name Length"]= data["Name"].str.len() 
  
# display 
data 