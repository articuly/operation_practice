# coding:utf-8
# author: Articuly
# datetime: 2020/6/18 17:55
# software: PyCharm

from flask import Flask, request
from settings import config
from hashlib import md5
import memcache

app = Flask(__name__)
app.config.from_object(config['development'])
mc = memcache.Client(['127.0.0.1:11211'], debug=True)


@app.route('/')
def index():
    print('full_path:', request.full_path)
    print(request.full_path.encode())
    print(md5(request.full_path.encode()).hexdigest())
    mc.set('username', 'artic')
    return mc.get('username') + 'hello'


# 启用缓存要注意缓存更新策略
# 内容发生更新后，需要更新缓存，比较复杂
# 一定时间后，缓存更新
@app.route('/page/<int:page>')
def get_lists(page):
    key = md5(request.full_path.encode()).hexdigest()
    print(key)
    res = mc.get(key)
    if res:
        return res + '<b>, read from memcached</b>'
    else:
        print('read from database')
        mc.set(key, 'this is {} page content'.format(page), time=10)
        return 'this is {} page content, <b>read from database</b>'.format(page)
