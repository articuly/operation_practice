# coding:utf-8
import rsa


class MyRsa:
    def __init__(self):
        # 不对称算法需要一对公钥与私钥
        pass

    def create_key_files(self, name):
        # 1024为设定你加密字符串的长度，
        # 最大可支持加密长度为512位=64字节，你也可以按需设置任意长度，越长加密越慢，越短越快
        pubkey, privkey = rsa.newkeys(2048)
        with open(name + '_public.key', 'wb') as f:
            f.write(pubkey.save_pkcs1())

        with open(name + '_private.key', 'wb') as f:
            f.write(privkey.save_pkcs1())

    def load_key_files(self, name):
        with open(name + '_public.key', 'rb') as f:
            self.pubkey = rsa.PublicKey.load_pkcs1(f.read())

        with open(name + '_private.key', 'rb') as f:
            self.privkey = rsa.PrivateKey.load_pkcs1(f.read())

    def out_public_key(self):
        print(self.pubkey)

    def out_private_key(self):
        print(self.privkey)

    def rsa_encrypt(self, string):
        content = string.encode('utf-8')
        res = rsa.encrypt(content, self.pubkey)
        return res

    def rsa_decrypt(self, crypto_res):
        content = rsa.decrypt(crypto_res, self.privkey)
        content = content.decode('utf-8')
        return content


if __name__ == '__main__':
    myrsa = MyRsa()
    while True:
        in_ = input('选择操作：\n1.生成密钥对\n2.RSA加密\n3.RSA解密\n4.退出程序')
        if in_ == '1':
            myrsa.create_key_files(input('证书名称：'))
        elif in_ == '2':
            keyname = input('证书名称：')
            myrsa.load_key_files(keyname)
            print('加密公钥，发给要加密沟通的人')
            myrsa.out_public_key()
            content = input('加密内容：')
            en_content = myrsa.rsa_encrypt(content)
            print('加密结果：', en_content)
        elif in_ == '3':
            keyname = input('证书名称：')
            myrsa.load_key_files(keyname)
            print('解密私钥，请勿外传')
            myrsa.out_private_key()
            try:
                de_content = myrsa.rsa_decrypt(en_content)
                print('解密结果：', de_content)
            except Exception as e:
                print('没有加密的内容')
                print(e)
        elif in_ == '4':
            break
