# coding:utf-8
# author: Articuly
# datetime: 2020/6/19 22:08
# software: PyCharm

from redis import StrictRedis

redis = StrictRedis('127.0.0.1')

# 列表类型
# 可以理解为python列表类型[val1, val2]
# redis中的列表实际上是链表结构类型

# 从右边插入项 - rpush(name,  val1, val2, val3)
# name -  变量名
# value - 添加项
redis.rpush('lst', 'a', 'b', 'c')
# 从左边插入项 - lpush(name, val1, val2, val3)
lists = redis.lpush('lst', 'A', 'B', 'C')
# 从右边弹出 - rpop(name) 阻塞弹出 brpop(name) - 如果没有可弹项，阻塞到有数据可弹为止
# 从左边弹出 - lpop(name) 阻塞弹出 blpop(name)
# 如果列表长度为0，返回 None
while True:
    try:
        data = redis.lpop('lst')
        print(data)
        if not data:
            break
    except Exception as e:
        print(e)
        break
