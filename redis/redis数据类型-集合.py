# coding:utf-8
# author: Articuly
# datetime: 2020/6/19 22:53
# software: PyCharm

from redis import StrictRedis

redis = StrictRedis('127.0.0.1')
# 集合类型
# 添加集合 - sadd(name,*value)
redis.sadd('sex', 'male', 'female')
# 获取集合 - smembers(name)
redis.smembers('sex')
# 随机弹出一项 - spop
redis.spop('sex')
# 判断某一值是否为集合成员 - sismember
redis.sismember('sex', 1)
# 返回所有的集合名称列表 - scan(cursor=0, count=None)
# cursor - 上次游标位置，0表示数据全部返回
# count - 每次返回数量
redis.scan()
