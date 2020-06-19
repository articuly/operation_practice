# coding:utf-8
# author: Articuly
# datetime: 2020/6/19 23:29
# software: PyCharm

from redis import StrictRedis

redis = StrictRedis(host="192.168.3.40")

# 有序集合类型
# 有序集合的每一项包含一个score值，根据这个score值可以对集合的项进行排序

# 添加有序集合 - zadd(name, mapping, nx=False, xx=False)
# name - 集合名
# mapping - {"item1":score, "item2":score}，由集合项与score组成的字典
# nx - 为True时，只能新增不存在的项
# xx - 为True时, 只能修改已经存在的项
# 添加一组有序集合，value为用户名，score为年龄，也就是rank集合由用户名与年龄组成
# 按照年龄排序
# user1: luxp, 28岁
# user2: wxp,  38岁
# user3: zxp,  27岁
redis.zadd('rank', {'luxp': 28, 'wxp': 38, 'zxp': 48, 'lsl': 32, 'artic': 28})
# 获取集合 -
# 返回列表 - zscan(name),第一项为cursor位置，为0表示数据已经全部返回
# 返回迭代器 - zscan_iter(name)
redis.zscan('rank')
items = redis.zscan_iter('rank')
# 计算集合中某个成员排名 - zrank(name, key)
# 计算luxp的排名(即根据年龄大小排序)
redis.zrank('rank', 'luxp')
# 提取排名在start, end之间成员 - zrange(name, start, end, desc=False, withscores=False)
# desc - 是否降序排列
# withscores - 是否返回score，以元组形式返回
redis.zrange('rank', 2, 4)
# 返回score值在min,max之间的项数 - zcount(name, min, max)
redis.zcount('rank', 27, 39)
# 删除 - zrem(name, value1, value2)
# 返回更改的项数
redis.zrem('rank', 'luxp')
# 根据score排序范围删除项 - zremrangebyrank(name, min, max)
# 根据score范围删除项 -  zremrangebyrank(name,min,max)
# 返回删除的项数
redis.zremrangebyrank("rank", 1, 3)
redis.zremrangebyscore("rank", 27, 28)
