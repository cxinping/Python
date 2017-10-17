import pymysql
import pandas as pd

db = pymysql.connect("127.0.0.1", "root", "123456", "mytestdb",charset="utf8" )
sql = 'select * from employee order by income desc'
df = pd.read_sql(sql, db, index_col=['id' ])
print(df)
