import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "mytestdb",charset="utf8" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(name,  \
          AGE, SEX, INCOME)  \
         VALUES ('%s',  '%d', '%s', '%d')" % \
      ('张三2',  21, 'F', 2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    print( e )
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
