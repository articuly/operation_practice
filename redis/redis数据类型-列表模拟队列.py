# coding:utf-8
# author: Articuly
# datetime: 2020/6/19 22:14
# software: PyCharm

from multiprocessing import Process
import time, random
from redis import StrictRedis

redis = StrictRedis('127.0.0.1')


# 使用redis的列表类型实现队列
# rpush + blpop 从右边插入数据，从左边弹出(FIFO)

def write2redis():
    n = 0
    while True:
        time.sleep(random.randint(1, 5))
        n += 1
        redis.rpush('queue', n)


def read2redis(pid):
    while True:
        # time.sleep(random.randint(0,3))
        # value = redis.lpop("queue")
        # 阻塞
        value = redis.blpop('queue')
        if value:
            print(pid, '=>', value)
        # print("无阻塞")
        print('阻塞消除')


if __name__ == '__main__':
    p1 = Process(target=write2redis)
    p2 = Process(target=read2redis, args=('p1',))
    p1.start()
    p2.start()
