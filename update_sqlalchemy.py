from select_sqlalchemy import session, Users
from sqlalchemy import or_

obj1 = session.query(Users).filter_by(user_id=20).one()
print(obj1)
# obj2 = session.query(Users).filter(Users.user_id > 30, Users.user_id < 50).all()
# print(obj2)
# obj3 = session.query(Users).filter(or_(Users.user_id == 55, Users.user_id == 77)).all()
# print(obj3)

print(dir(obj1))
print(obj1.username, obj1.realname, obj1.password, obj1.age)

obj1.age = 98
session.commit()

obj = session.query(Users).filter_by(user_id=20).one()
print(obj.username, obj.age)
