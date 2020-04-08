from select_sqlalchemy import session, Users
from sqlalchemy import or_

obj1 = session.query(Users).filter_by(user_id=444).one()
print(obj1)
obj2 = session.query(Users).filter(Users.user_id > 30, Users.user_id < 50).all()
print(obj2)
obj3 = session.query(Users).filter(or_(Users.user_id == 55, Users.user_id == 77)).all()
print(obj3)


def get_user():
    objs = session.query(Users).filter(Users.user_id > 485, Users.user_id < 495).all()
    return objs


for obj in get_user():
    print(obj.username)

# 删除
session.delete(get_user()[0])
session.commit()

print('*' * 50)
for obj in get_user():
    print(obj.username)
