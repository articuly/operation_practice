# coding:utf-8
# author: Articuly
# datetime: 2020/6/19 16:20
# software: PyCharm

from flask import Flask, request, jsonify, render_template
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('localhost', 27017)
db = client.blog

# 使用mongodb作为注册登陆数据库
users = db.users


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'POST':
        user = users.find_one({'username': request.form['username']})
        print(user['password'])
        if user['password'] == request.form['password']:
            print(user['username'], 'has login')
            return jsonify({'result': 'success'})
    return render_template('login.html')


@app.route('/register', methods=['get', 'post'])
def register():
    if request.method == 'POST':
        user = {
            'realname': request.form['name'],
            'username': request.form['username'],
            'password': request.form['password'],
            'sex': request.form['sex'],
            'mylike': '|'.join(request.form.getlist('like')),
            'city': request.form['city'],
            'intro': request.form['intro']
        }
        try:
            # 一般结合mysql使用
            # mongodb中记录读取频繁的数据
            # 另外还要设置索引
            res = users.insert(user)
        except:
            print('insert fail')
        return jsonify({'_id': str(res)})
    return render_template('register.html')

