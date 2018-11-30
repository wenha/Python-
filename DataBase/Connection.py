import pymysql

# 打开数据库
db = pymysql.connect('localhost','wenha','123456','test')

# 使用Cursor方法创建一个游标对象
cursor = db.cursor()

# 使用Execute方法执行SQL查询
cursor.execute('SELECT VERSION()')

# 使用fetchone方法获取单条数据
data = cursor.fetchone()

print('DataBase Version: %s' % data)

# 关闭数据库连接
db.close()