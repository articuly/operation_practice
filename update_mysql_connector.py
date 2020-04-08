from mysql import connector

cnx = connector.Connect(user='root', host='127.0.0.1', password='123456', database='mycms')
cursor = cnx.cursor()


def get_user():
    sql = "select * from `users` where user_id=7"
    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)


get_user()

# sql1 = "insert into `users` set password='123456', username='articuly3'"
sql2 = "update `users` set age=99 where user_id=7"
try:
    # cursor.execute(sql1)
    cursor.execute(sql2)
    cnx.commit()
except Exception as e:
    print(e)
    cnx.rollback()

# 影响条数
res = cursor.rowcount
print('影响', res)

cursor.close()
cnx.close()
