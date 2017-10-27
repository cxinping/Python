import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

df = ts.get_tick_data('600848',date='2014-01-09')
df =df.set_index('time')
df =df.sort_index()

df['price'].plot()