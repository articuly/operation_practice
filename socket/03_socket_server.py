from socket import *

# 创建socket对象
s_server = socket(AF_INET, SOCK_STREAM)

# 绑定IP与端口号
s_server.bind(("127.0.0.1", z))

# 开始监听
s_server.listen()

client_sock, client_addr = s_server.accept()
print("waiting...........")
print(client_sock, client_addr)
print("-" * 50)

# 创建一个永久循环
while True:
    message = client_sock.recv(1024)
    # message 是字节，需要解码
    message = message.decode("utf-8")
    if not message:
        continue
    if message == "quit":
        # 发出关闭信号
        client_sock.close()
        break
    else:
        print("客户端消息>>>", message)
        client_sock.send(b"continue...")

s_server.close()
print("服务器关闭")
