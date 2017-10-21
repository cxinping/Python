import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

data = ts.get_hist_data('600848')
print(data.index)
#前5条记录
data = data.head(5)

data['open'].plot()

plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()



