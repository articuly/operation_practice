# coding:utf-8
# author: Articuly
# datetime: 2020/6/19 19:05
# software: PyCharm

from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1')

# 字符串类型
# 设置一个键 - set(name, value, ex=None, px=None, nx=False, xx=False)
# ex - 设定过期时间，单位 秒
# px - 设定过期时间，单位 微秒
# nx - 设为True，name不存在时才能set
# xx - 设为True， name存在时才能set
redis.set('username', 'articuly')
redis.set('website', 'articuly.com', ex=10)
# 获取一个键 - get(name)
# 返回类型为bytes类型
username = redis.get('username')
website = redis.get('website').decode()
# 数值加减
# incr, decr
redis.set('number', 10)
redis.incr('number', 100)
print(redis.get('number'))
redis.decr('number', 50)
print(redis.get('number'))
