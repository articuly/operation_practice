from socket import socket, AF_INET, SOCK_STREAM

# AF_INET  - IPV4 协议
# SOCK_STREAM - 套接字类型为面向连接的可靠字节流
# 创建socket对象
s_server = socket(AF_INET, SOCK_STREAM)

# 绑定IP与端口号
s_server.bind(("127.0.0.1", 8000))

# 开始监听
s_server.listen()

# 等待请求，在没有请求到来之前，会一直等待（堵塞）
print("waiting...........")
client_sock, client_addr = s_server.accept()
print(client_sock, client_addr)
print("-" * 50)
client_sock.close()
s_server.close()
print("服务器关闭")
