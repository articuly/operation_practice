# coding:utf-8
# author: Articuly
# datetime: 2020/6/19 21:53
# software: PyCharm

from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1')

# hash类型
# 可以理解为python字典类型{"key1":val, "key2":val}

# 设置一个键 - hset(name, key, value)
# name - 变量名
# key - 添加的key
# value - 添加的key对应的值
# 给userinfo 添加了一个username，值为articuly
redis.hset('userinfo', 'username', 'articuly')
redis.hset('userinfo', 'age', 30)
redis.hset('userinfo', 'sex', 1)
# 获取字典 - hgetall(name)
# 返回name的全部项
userinfo = redis.hgetall('userinfo')
# 获取字典中的某一项 - hget(name, key)
# 返回name中的key项,不存在返回None
redis.hget('userinfo', 'age')
redis.hget('userinfo', 'name')
# 获得字典的长度 - hlen(name)
redis.hlen('userinfo')
# 获得所有的key - hkeys(name)
redis.hkeys('userinfo')
# 获得所有的value - hvals(name)
redis.hvals('userinfo')
# 获取name的多个key值 - hmget(name, "key1", "key2")
redis.hmget('userinfo', 'username', 'age')
# 加减操作
# hincrby(name, key, amount=1)
redis.hincrby('userinfo', 'age', 10)
redis.hincrby('userinfo', 'age', 5)
# 删除key - hdel(name, key1,key2)
# 返回删除的项数
redis.hkeys('userinfo')
redis.hdel('userinfo', 'age')
redis.hkeys('userinfo')
