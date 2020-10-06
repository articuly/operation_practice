# -*- coding: utf-8 -*-
# http服务器

from wsgiref.simple_server import make_server
from application import simple_app

port = 8000
server = make_server('127.0.0.1', port, simple_app)
print("服务器启动，端口号：%d" % port)
server.serve_forever()
