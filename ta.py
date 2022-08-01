import numpy as np
from numpy import genfromtxt
import talib

my_data = genfromtxt('15minutes.csv', delimiter=',')

print(my_data)

close = my_data[:, 4]

print(close)

# moving_average = talib.SMA(close, timeperiod=10)

# print(moving_average)

rsi = talib.RSI(close)

print(rsi)