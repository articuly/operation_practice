# coding:utf-8
# author: Articuly
# datetime: 2020/6/18 22:44
# software: PyCharm

import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)

# 数据库名为blog
db = client.blog

# 插入数据
# 两条user信息结构相同，但是一条网站信息结构不一样
# 对于mongodb来讲，每一条之间都是完全独立的文档
user = [{"username": "articuly", "sex": "man", "age": 16},
        {"username": "luxp", "sex": "man", "age": 28},
        {"web_url": "python-xp.com", "type": "技术类", "company": "平哥编程"}]

# 使用insert插入一条记录
# users自动创建
# insert_one
db.users.insert_one(user[0])
# 一次性插入多个记录
# insert_many
res = db.users.insert_many(user)
# 查找数据
# 找到用户名为artic的用户
# mongodb使用json格式来表示查询条件
# 在python客户端中以字典提供查询条件
# {"username":"artic"}
# {"username":"lxp", "age":28}
# 正则匹配 {"username":"/xp/"}
u1 = db.users.find_one({'username': 'articuly'})
u2 = db.users.find({'username': 'artic'})
# 根据 _id 查q
from bson import ObjectId

id = '5eeb8875cab6435a8a58a4ba'
id = ObjectId(id)
u3 = db.users.find_one({'_id': id})
# 修改
# update_one
# update_many
u4 = db.users.find_one({'username': 'articuly'})
u4['age'] = 30
u4['sex'] = 'man'
res = db.users.update({'_id': u4['_id']}, u4)
# 删除
# 删除web_url这项
# delete_many - 删除多条
res = db.users.delete_one({'web_url': 'python-xp.com'})
res.delete_count
res.raw_result
# 删除大于20岁的
res = db.users.delete_many({'age': {'$gt': 20}})
