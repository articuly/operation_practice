from select_sqlalchemy import session, Users
from sqlalchemy import or_

obj1=session.query(Users).filter_by(user_id=99).one()
print(obj1)