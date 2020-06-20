# coding:utf-8
# author: Articuly
# datetime: 2020/6/20 8:00
# software: PyCharm

from hashlib import md5
from uuid import uuid4
import json
from flask import Flask, request, session, url_for, redirect
from redis import StrictRedis

app = Flask(__name__)
app.secret_key = "123456"
redis = StrictRedis('127.0.0.1')


@app.route('/login')
def login():
    # 用户验证难过
    pass
    user = {'user': 'articuly', 'age': 30}
    if user:
        session_id = set_redis_session()
        print(session_id)
        redis.hmset(session_id, user)
    return '<a href=' + url_for('dosomething') + '>登陆成功 {}</a>'.format(session.get('session_id'))


@app.route('/do')
def dosomething():
    # 根据session_id从redis中取值
    if session.get('session_id') and redis.exists(session['session_id']):
        user = redis.hgetall(session['session_id'])
        user = {key.decode(): val.decode() for key, val in user.items()}
    else:
        return redirect(url_for('login'))
    return json.dumps(user)


def set_redis_session():
    # 检查session_id是否存在
    session_id = session.get('session_id')
    if not session_id:
        session_id = uuid4().hex
        session['session_id'] = session_id
    return session_id


def get_redis_session():
    session_id = session.get('session_id')
    print(session_id)
    # session_data=redis.hgetall(session_id)
    session_data = None
    return session_data


if __name__ == "__main__":
    app.run(port="8002", debug=True)
