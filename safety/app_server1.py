# coding:utf-8
import base64
from flask import Flask
import requests
from RSA_en import MyRsa
from AES_en import decrypt_content

app = Flask(__name__)

# 第三方接口，比如支付宝、微信接口
SEVER_2 = "http://127.0.0.1:8002"


@app.route('/get_key')
def get_key():
    # 发送密钥
    key = '1234567890abcdef'
    print('key:', key)
    # 加载server2密钥 - 实际上server1只有server2的公钥
    server2_rsa = MyRsa()
    server2_rsa.load_key_files('server2')
    # 将key用server2的公钥加密
    data = server2_rsa.rsa_encrypt(key)
    print('rsa_encrypt', data)
    # 进行编码
    # 编码结果转换为字符串
    # 这一步非必须，如果在url地址上只能使用字符串
    # data = data.decode()
    data = base64.b64encode(data)
    print('base64_encode', data)
    # 向server2发送加密数据
    res = requests.post(SEVER_2 + '/validate_key', {'data': data}).content
    print('return data', res)
    # 用server1私钥解密
    server1_rsa = MyRsa()
    server1_rsa.load_key_files('server1')
    # 得到私钥解密结果
    # 该结果还需要继续使用AES对称解密
    res = server1_rsa.rsa_decrypt(res)
    print('rsa_decrypt', res)
    # 进行对称解密
    # 如果解密后结果正确，表示服务器身份与加密算法都没有问题
    decode_key = decrypt_content(res, 'AES', key, 'utf-8')
    print('base64_decode', decode_key)
    if key == decode_key:
        return '服务器不是伪造'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)
