#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Host": "127.0.0.1:5000",
    "Proxy-Connection": "keep-alive",
    "Referer": "",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
head = ""
for i in headers:
    head += i + ":" + headers[i] + "\r\n"

head = "TRACE / HTTP/1.1\r\n" \
       + head + \
       "Connection: close\r\n\r\n"
web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
web_socket.connect(("127.0.0.1", 5000))
web_socket.send(bytes(head, encoding="utf-8"))

buff = []
while True:
    data = web_socket.recv(1024).decode("utf-8")
    if data:
        buff.append(data)
    else:
        break
web_socket.close()

print(head)
print('*' * 30)
print(''.join(buff))
