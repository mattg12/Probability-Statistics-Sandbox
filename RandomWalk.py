#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Random Walk
Created on Wed Mar  6 15:48:58 2019

@author: mattg
"""

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller

days = 248
t = 1/days
s = 100
vol = 0.157

random = np.random.normal(size=days)

prices = []

for i in range(len(random)):
    if i == 0:
        prices.append(s)
    else:
        price = prices[i-1]*np.exp(-.5*(vol**2)*t + vol*np.sqrt(t)*random[i])
        prices.append(price)
        
plt.figure(figsize=(10,7))

plt.plot(prices)
plt.title('Brownian Motion', fontsize=18)
plt.xlabel('Days', fontsize=14)
plt.ylabel('Asset Price', fontsize=14)

df = pd.DataFrame({'Day':range(days),'Asset_Price':prices})

df['Returns'] = df['Asset_Price'].diff()

plt.figure(figsize=(10,7))

plt.hist(df['Returns'], bins=20)
plt.title('Distribution of Returns', fontsize=18)

ax = plot_acf(df['Asset_Price'], zero=False)

df.index = pd.DatetimeIndex(start='2012-01-01', periods=df.shape[0], freq='D')


ar1 = ARIMA(endog=df['Asset_Price'], order=(1,0,0))
model = ar1.fit()

model.summary()

X = df['Asset_Price']
result = adfuller(X)
print('ADF Statistic: {}'.format(result[0]))
print('p-value: {}'.format(result[1]))
print('Critical Values:')
for key, value in result[4].items():
    print('\t{}: {}'.format(key, round(value, 3)))