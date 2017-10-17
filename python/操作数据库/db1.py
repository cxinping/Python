import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "mydb",charset='utf8')


# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO test1(id,num)
         VALUES (2, '王五' )"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    # 如果发生错误则回滚
    print(e)
    db.rollback()

# 关闭数据库连接
db.close()
