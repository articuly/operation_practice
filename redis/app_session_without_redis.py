# coding:utf-8
# author: Articuly
# datetime: 2020/6/20 8:00
# software: PyCharm

import json
from flask import Flask, request, session, url_for

app = Flask(__name__)
app.secret_key = "123456"


@app.route('/login')
def login():
    # 用户验证难过
    pass
    user = {'user': 'articuly', 'age': 30}
    if user:
        session['user'] = user
    return '<a href=' + url_for('dosomething') + '>登陆成功</a>'


@app.route('/do')
def dosomething():
    user = session.get('user')
    return json.dumps(user)


if __name__ == "__main__":
    app.run(port="8001", debug=True)
