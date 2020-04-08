from select_sqlalchemy import session, Users
from math import ceil

# 常量，每页显示的条数
PAGE_SIZE = 100

total = session.query(Users).count()
print(total)

total_page = ceil(total / PAGE_SIZE)
print(total_page)

CURRENT_PAGE = 10
start = (CURRENT_PAGE - 1) * PAGE_SIZE

res = session.query(Users).offset(start).limit(PAGE_SIZE).all()
for item in res:
    print(item.user_id, item.username)
