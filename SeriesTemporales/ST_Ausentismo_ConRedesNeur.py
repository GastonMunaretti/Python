# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 09:47:47 2020

@author: gmunaretti

Prediccion con redes neuronales
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


plt.plot(meses['2019'].values)
plt.plot(meses['2018'].values)


Periodo_2018 = df['2018-12-21':'2018-12-31']
plt.plot(Periodo_2018.values)

Periodo_2019 = df['2019-01-01':'2019-12-20']
plt.plot(Periodo_2019.values)


Periodo_20 = df['2018-12-21':'2019-12-20']
plt.plot(Periodo_20.values)

ts = df['2018-12-21':'2019-12-20']

PASOS = 7

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg
 
# load dataset
values = df.values
# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(-1, 1))
values=values.reshape(-1, 1) # esto lo hacemos porque tenemos 1 sola dimension
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = series_to_supervised(scaled, 7, 1)
reframed.head()



# split into train and test sets
values = reframed.values
n_train_days = 11+352 - (30+7)
train = values[:n_train_days, :]
test = values[n_train_days:, :]
# split into input and outputs
x_train, y_train = train[:, :-1], train[:, -1]
x_val, y_val = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
x_train = x_train.reshape((x_train.shape[0], 1, x_train.shape[1]))
x_val = x_val.reshape((x_val.shape[0], 1, x_val.shape[1]))
print(x_train.shape, y_train.shape, x_val.shape, y_val.shape)



##########################################################################################

"""La arquitectura de la red neuronal será:

Entrada 7 inputs, como dijimos antes
1 capa oculta con 7 neuronas (este valor lo escogí yo, pero se puede variar)
La salida será 1 sola neurona
Como función de activación utilizamos tangente hiperbólica puesto que utilizaremos valores entre -1 y 1.
Utilizaremos como optimizador Adam y métrica de pérdida (loss) Mean Absolute Error
Como la predicción será un valor continuo y no discreto, para calcular el Acuracy utilizaremos Mean Squared Error y para saber si mejora con el entrenamiento se debería ir reduciendo con las EPOCHS.
"""


def crear_modeloFF():
    model = Sequential() 
    model.add(Dense(PASOS, input_shape=(1,PASOS),activation='tanh'))
    model.add(Flatten())
    model.add(Dense(1, activation='tanh'))
    model.compile(loss='mean_absolute_error',optimizer='Adam',metrics=["mse"])
    model.summary()
    return model



""" 
Entrenamiento y Resultados
Veamos cómo se comporta nuestra máquina al cabo de 40 épocas.
En la gráfica vemos que los puntitos verdes intentan aproximarse a los rojos. 
Cuanto más cerca ó superpuestos mejor. TIP: Si aumentamos la cantidad de EPOCHS mejora cada vez más.

"""
EPOCHS=400
 
model = crear_modeloFF()
 
history=model.fit(x_train,y_train,epochs=EPOCHS,validation_data=(x_val,y_val),batch_size=PASOS)


# Visualizamos al conjunto de validación (recordemos que eran 30 días)

results=model.predict(x_val)
plt.scatter(range(len(y_val)),y_val,c='g')
plt.scatter(range(len(results)),results,c='r')
plt.title('validate')
plt.show()












