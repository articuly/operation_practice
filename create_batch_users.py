# coding:utf-8
import mysql.connector as connector
import random

cnx = connector.connect(user='root', password='123456', host='127.0.0.1', database='mycms')
cursor = cnx.cursor()

users = []
words = list('abcdefghijklmnopqrstuvwxyz')
cities = ['010', '020', '021', '023', '0755', '0571', '0512']
hobbies = ['travel', 'reading', 'singing', 'dancing', 'writing', "swimming", "playing basketball"]


# 只有检测可用才会返回
def create_user_name():
    while True:
        random.shuffle(words)
        username = ''.join(random.choices(words, k=random.randint(6, 15)))
        if not check_user(username) and username not in users:
            users.append(username)
            break
    print('>' * 3, username)
    return username


# 查询用户名在数据库是否存在
def check_user(username):
    sql = "select * from `users` where username='{username}'"
    try:
        cursor.execute(sql.format(**{'username': username}))
    except connector.Error as e:
        print(e)
    res = cursor.fetchone()
    return res


# 批量创建N条数据
def create_batch_users(n):
    sql_list = []
    sql = 'insert into `mycms`.`users` values'
    for i in range(n):
        username = create_user_name()
        user = {
            'id': i,
            'realname': ''.join(random.choices(words, k=6)),
            'username': username,
            'password': random.randint(111111, 999999),
            'city': random.choice(cities),
            'age': random.randint(15, 45),
            'sex': random.choice(['男', '女']),
            'hobby': ','.join(random.choices(hobbies, k=random.randint(0, 3)))
        }
        values = "(null, '{username}', '{realname}', '{password}', default, '{sex}', '{hobby}','{city}', '{age}')".format(
            **user)
        # print('values:', values)
        sql_list.append(values.format(**user))
        # print('sql_list:', sql_list)
    try:
        sql += ','.join(sql_list)
        print('sql:', sql)
        cursor.execute(sql)
        cnx.commit()
    except connector.Error as e:
        print('error:', e)
        cursor.close()
        cnx.close()


for i in range(10):
    create_batch_users(1000)
