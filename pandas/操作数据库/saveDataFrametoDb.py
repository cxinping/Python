from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/mytestdb?charset=utf8')
sdata1 = {'name' : ['王五1','王五2'], 'age' : [99, 87], 'sex':['M','M'] , 'income':[5000,6000]   }
df1 = pd.DataFrame(sdata1 )
df1.to_sql('employee2', con=engine, if_exists='append')
print( df1 )
