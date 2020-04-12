# coding:utf-8
import mysql.connector as connector
from concurrent.futures import ThreadPoolExecutor
from mysql.connector import pooling
import random

# cnx = connector.connect(user='root', password='123456', host='127.0.0.1', database='mycms')
# cursor=cnx.cursor()
cnxpool = pooling.MySQLConnectionPool(pool_name='mypool', pool_size=32, user='root', host='localhost', database='mycms',
                                      password='123456')
users = []
words = list('abcdefghijklmnopqrstuvwxyz')
# cities = ['010', '020', '021', '023', '0755', '0571', '0512']
hobbies = ['钓鱼', '旅游', '看书', '唱歌']


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
    try:
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
    except Exception as error:
        print(error)
        return False
    sql = "select * from `users` where username='{username}'"
    try:
        cursor.execute(sql.format(**{'username': username}))
    except connector.Error as e:
        print(e)
    res = cursor.fetchone()
    return res


# 批量创建N条数据
def create_batch_users(n):
    try:
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
    except Exception as error:
        print(error)
        return False
    sql_list = []
    sql = 'insert into `users` values'
    for i in range(n):
        username = create_user_name()
        user = {
            'realname': ''.join(random.choices(words, k=6)),
            'username': username,
            'password': random.randint(111111, 999999),
            'age': random.randint(15, 45),
            'sex': random.choice(['男', '女']),
            'hobby': ','.join(random.choices(hobbies, k=random.randint(0, 3)))
        }
        values = "(null, '{username}', '{realname}', '{password}', default, default, '{age}', '{sex}', '{hobby}', default, default)".format(
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


# for i in range(500):
#     create_batch_users(1000)
if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    pool.submit(create_batch_users(10000))
