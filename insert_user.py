import mysql.connector as connector

cnx = connector.connect(user='root', password='123456', host='127.0.0.1', database='mycms')

cursor = cnx.cursor()


def createUser(user):
    sql = "insert into `users` (`user_id`,`username`,`realname`,`password`,`sex`) values (null, '{username}','{realname}','{password}','{sex}');"

    sql = sql.format(**user)  # 解包关键词参数的值
    res = None
    print(sql)
    try:
        cursor.execute(sql)
        cnx.commit()
        print(dir(cursor))
        res = cursor.lastrowid  # 最后一行的id
    except Exception as e:
        print(e)
    return res


user = {'username': 'articuly2',
        'realname': 'articuly2',
        'password': '123456',
        'sex': '男'}

res = createUser(user)
print('数据插入的结果：', res)
