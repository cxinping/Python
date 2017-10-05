import pandas as pd
 
# Reading data locally
#df = pd.read_csv('./data.csv')
 
# Reading data from web
data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
df = pd.read_csv(data_url)



