from mysql import connector
from threading import Thread


def update_age(age):
    sql = "update `users` set age={age} where user_id=3 and age is null"
    sql = sql.format(age=age)
    cnx = connector.connect(user='root', password='123456', host='127.0.0.1', database='mycms')
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
        # cnx.commit()
        print('age={0}, 影响条数：{1}'.format(age, cursor.rowcount))
    except Exception as e:
        print(e)
        cnx.rollback()
    cursor.close()
    cnx.close()


# 模拟多人并发
for i in range(1, 11):
    t = Thread(target=update_age, args=(i,))
    t.start()
