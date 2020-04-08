from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建数据库引擎，连接mqsql数据库，用pymysql方式
engine = create_engine('mysql+pymysql://root:123456@localhost/mycms')

# 创建会话对象，根据不同的数据库引擎创建对应的会话对象
Session = sessionmaker(bind=engine)
# 创建会话对象实例
session = Session()

# base为映射基类
Base = declarative_base()


# 数据库表模型的映射
class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(32))
    realname = Column(String(32))
    password = Column(String(32))
    age = Column(Integer)
    city = Column(String(32))


if __name__ == '__main__':
    res = session.query(Users, Users.username, Users.realname).filter(Users.username.like("py%")).limit(50).all()
    print(res)
