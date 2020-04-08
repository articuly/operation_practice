from select_sqlalchemy import session, Users
from sqlalchemy import func

res = session.query(Users).count()
print(res)

# TODO count
res = session.query(func.count(1), Users.city).group_by(Users.city).all()
print('count', res)

res = session.query(func.avg(Users.age), Users.city).group_by(Users.city).all()
print('avg', res)

res = session.query(func.sum(Users.age), Users.city).group_by(Users.city).all()
print('sum', res)

res = session.query(func.max(Users.age), Users.city).group_by(Users.city).all()
print('max', res)
