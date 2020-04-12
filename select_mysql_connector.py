import mysql.connector as cn

cnx = cn.connect(user='root', password='123456', host='127.0.0.1', database='mycms')
cursor = cnx.cursor()

sql = "select * from `users` where age=26"
cursor.execute(sql)
res1 = cursor.fetchone()
print(res1)
res2 = cursor.fetchmany(50)
print(res2)
# res3 = cursor.fetchall()
# print(res3)
