# coding:utf-8
# author: Articuly
# datetime: 2020/6/18 17:34
# software: PyCharm

import memcache
import sys, time, random
from multiprocessing import Process

# memcached 内容可以被多个进程共享
args = sys.argv
print(args)

host = '127.0.0.1:11211'
mc = memcache.Client([host], debug=True)

# memcached集群[(host:port,weight)]
# mc = memcached.Client([('ip:port', 1),('ip:port', 1)], debug=True)

# 添加-add  修改-replace 删除-delete 取值 - get
# mc.add(key, value, time)
# mc.set(key, value, time)
# time 过期时间
'''
mc.set('name', 'artic')
mc.set('name', 'artic', 3)
name = mc.get('name')

# mc.replace(key,value)，如果key不存在，返回False
mc.replace('name', 'articuly', 3)
mc.set('name', 'articuly', 3)

# 一次set多个值
dicts = {'key1': 10, 'key2': 20, 'key3': 30}
mc.set_multi(dicts)

# 删除
mc.delete('key1')
mc.delete_multi(['key1', 'key2'])

# 一次取出多个值
mc.get_multi(['key2', 'key3'])

# 加减
mc.incr('key3', 10)
mc.decr('key3', 5)

# 清空
mc.flush_all()
'''


# 多进程共享数据
def write2mem(server):
    mc = memcache.Client(server, debug=True)
    while True:
        time.sleep(3)
        print('writing memcached')
        mc.set('key1', random.random())


def read2mem(server):
    mc = memcache.Client(server, debug=True)
    while True:
        value = mc.get('key1')
        if value:
            print('now, value is', value)
            mc.delete('key1')


if __name__ == '__main__':
    server = [host]
    p1 = Process(target=write2mem, args=(server,))
    p2 = Process(target=read2mem, args=(server,))
    p1.start()
    p2.start()
