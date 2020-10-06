from socket import *

# 创建一个socket对象
c_client = socket(AF_INET, SOCK_STREAM)
c_client.connect(("127.0.0.1", 8000))

while True:
    message = input("请输入消息：")
    if not message:
        continue
    c_client.send(bytes(message, encoding="utf-8"))

    if message == "quit":
        break
    result = c_client.recv(1024)
    print(result.decode("utf-8"))

c_client.close()
