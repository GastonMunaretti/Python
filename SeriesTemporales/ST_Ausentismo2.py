# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:52:26 2020

@author: gmunaretti
"""


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
# matplotlib inline
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('fast')

from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('Ausentismo_Diario_Arima.csv',  parse_dates=[0], header=None,index_col=0, squeeze=True,names=['fecha','unidades'])
 
print(df.index.min())
print(df.index.max())

#--------------------------------------------------------------------------------------------

print(len(df['2018']))
print(len(df['2019']))

#--------------------------------------------------------------------------------------------
# Visualización de datos
df.describe()

#--------------------------------------------------------------------------------------------

meses =df.resample('M').mean()
meses

#--------------------------------------------------------------------------------------------


#plt.plot(meses['2019'].values)
#plt.plot(meses['2018'].values)


#Periodo_2018 = df['2018-12-21':'2018-12-31']
#plt.plot(Periodo_2018.values)

#Periodo_2019 = df['2019-01-01':'2019-12-20']
#plt.plot(Periodo_2019.values)


#Periodo_20 = df['2018-12-21':'2019-12-20']
#plt.plot(Periodo_20.values)

#ts = df['2018-12-21':'2019-12-20']

# graficando 
plot = df.plot(figsize=(10, 8))

















