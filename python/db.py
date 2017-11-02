import pymysql
import traceback as tbk

host = '127.0.0.1'
user='root'
password='123456'
port=3306
database = 'mytestdb'
charset='utf8'

def insertData():
    db = pymysql.connect(host=host,user=user,password=password, 
                     database=database,port=port, charset=charset)
    
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    
    # SQL 插入语句
    sql = "insert into employee(name, age,sex, income)  \
            values( '{0}' , {1}, '{2}' , {3} )".format('李四', 20, 'F', 5000)
    
    updateSql = "update employee set name='{0}', age={1}  \
            where id ={2}".format('wangwu', 24, 1)
    
    
    try:
        # 执行sql语句
        cursor.execute(updateSql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        print(e)
        db.rollback()
    
    # 关闭数据库连接
    db.close()

def delData():
    db = pymysql.connect(host=host,user=user,password=password, 
                     database=database,port=port, charset=charset)
    
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    
    # SQL 插入语句
    sql = "del from employee where id={0}".format(1)
         
    try:
        # 执行sql语句
        cursor.execute( sql  )
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        print(e)
        db.rollback()
    
    # 关闭数据库连接
    db.close()
    
def querylData():
    db = pymysql.connect(host=host,user=user,password=password, 
                     database=database,port=port, charset=charset)
    
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    
    # SQL 插入语句
    sql = "select *  from employee where id > 1 "
         
    try:
        # 执行sql语句
        cursor.execute( sql  )
        # 提交到数据库执行
        data = cursor.fetchall()
        print( data , type(data ))
#        data = cursor.fetchone()
#        print( data , type(data ))
        print( '*** rowcount=' , cursor.rowcount )
    except Exception as e:
        # 如果发生错误则回滚
        print(e)
        
    
    # 关闭数据库连接
    db.close()

querylData()    