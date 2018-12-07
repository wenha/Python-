import pymysql

# 打开数据库
db = pymysql.connect('localhost','wenha','123456','test')

# 使用Cursor获取操作游标
cursor = db.cursor()

# SQ插入语句
sql = "insert into Employee(Name,Sex) values('张三','M')"

try:
    # 执行SQL语句
    cursor.execute(sql)

    # 提交到数据库
    db.commit()

except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()