# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:14:36 2020

@author: gmunaretti
"""

from datetime import datetime
date_string = "21 June, 2018"
print("date_string =", date_string)
print("type of date_string =", type(date_string))
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
print("type of date_object =", type(date_object))