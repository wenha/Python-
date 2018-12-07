import pymysql

# 打开数据库连接
db = pymysql.connect('localhost','wenha','123456','Test')

cursor = db.cursor()

sql = 'select * from employee where id > 500'

try:
    # 执行SQL语句
    cursor.execute(sql)

    # 获取所有记录列表
    results = cursor.fetchall()

    for row in results:
        fname = row[0]
        lname = row[1]
        sex = row[2]

        print(fname,lname,sex)

except:
    print('Error')

db.close()