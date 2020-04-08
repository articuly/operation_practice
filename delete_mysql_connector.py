from mysql import connector

cnx = connector.connect(user='root', password='123456', host='127.0.0.1', database='mycms')
cursor = cnx.cursor()

sql = "delete from `users` where `user_id` between 110 and 120;"
cursor.execute(sql)
res = cursor.rowcount
print(res)
cnx.commit()

cursor.close()
cnx.close()
