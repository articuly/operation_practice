from socket import *

# 创建一个socket对象
c_client = socket(AF_INET, SOCK_STREAM)
c_client.connect(("127.0.0.1", 8000))
c_client.close()
