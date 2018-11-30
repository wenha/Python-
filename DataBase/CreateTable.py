import pymysql

# 打开数据连接
db = pymysql.connect('localhost', 'wenha', '123456', 'test')

# 使用Cursor方法获取操作游标
cursor = db.cursor()

# 执行SQL语句
cursor.execute('drop table if exists Employee')

sql = """Create table Employee(
    Id int not null primary key,
    Name char(20) not null,
    Sex char(2)
)"""

cursor.execute(sql)

# 关闭连接
db.close()