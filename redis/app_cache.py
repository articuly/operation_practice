# coding:utf-8
# author: Articuly
# datetime: 2020/6/19 23:40
# software: PyCharm

from hashlib import md5
from flask import Flask, request
from redis import StrictRedis

app = Flask(__name__)
redis = StrictRedis('127.0.0.1')


# 向redis写入数据
@app.route('/page/<int:page>')
def get_page(page):
    keyname = md5(request.full_path.encode()).hexdigest()
    content = redis.get(keyname)
    if not content:
        # 从数据库获取数据
        pass
        content = f'第{page}页'
        redis.set(keyname, content, ex=5)
        content += '--来自数据库'
    else:
        content = content.decode() + '--来自redis'
    return content


if __name__ == '__main__':
    app.run(debug=True)
