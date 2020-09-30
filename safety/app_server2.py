# coding:utf-8
import base64
from flask import Flask, request
from RSA_en import MyRsa
from AES_en import encrypt_content

app = Flask(__name__)


@app.route('/validate_key', methods=['post'])
def send_key():
    # 获取发送过来的数据
    data = request.form['data']
    # base64解码
    # 如果数据是字符串类型，需要data.encode()转换为字节类型
    data = base64.b64decode(data)
    # 使用server2的私钥解密
    server2_rsa = MyRsa()
    server2_rsa.load_key_files('server2')
    # server2使用私钥解密
    data = server2_rsa.rsa_decrypt(data)
    data = encrypt_content(data, 'AES', data, 'utf-8')
    # 最后用server1的公钥加密
    server1_rsa = MyRsa()
    server1_rsa.load_key_files('server1')
    res = server1_rsa.rsa_encrypt(data)
    return res


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8002, debug=True)
