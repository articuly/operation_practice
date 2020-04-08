from select_sqlalchemy import session, Users
from sqlalchemy import func

res = session.query(Users, Users.user_id, Users.username, Users.city).order_by(Users.user_id.desc()).limit(100).offset(
    10).all()
for item in res:
    print(item)
