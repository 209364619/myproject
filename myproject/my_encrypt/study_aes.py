# coding=utf-8
from Crypto.Cipher import AES
from Crypto import Random
from pkcs7 import PKCS7Encoder
import base64
from binascii import b2a_hex, a2b_hex
from hashlib import md5


class AES_ENCRYPT():
    def __init__(self):
        # IV = '2015030120123457'  #为了结合前端js 这里改为了EBC模式，没有了偏移量
        # self.iv = IV
        # 密钥
        AES_SECRET_KEY = "0123456789123456"
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_ECB  # CBC模式

    # 加密函数
    def encrypt(self, text):
        '''
        对传入字符串进行加密
        :param text:
        :return: base64 字符串
        '''
        # 将文本处理为编码需要的格式
        encode = PKCS7Encoder()  # PKCS7
        encode_text = encode.encode(text)  # 编码格式
        # 使用密钥进行加密
        crypto = AES.new(self.key, self.mode)
        crypto_text = crypto.encrypt(encode_text)
        # 将文本处理为控制台能够输出的形式，除了base64 也可以使用a2b_hex（这里为了对应前端js的处理，
        # 使用base64进行输出）
        console_enable_text = base64.b64encode(crypto_text)
        return console_enable_text

    def unencrypt(self, text):
        '''
        解密方法
        :param text: 字符串文本
        :return: 字符串原文
        '''
        # base64解码字符串
        text_base64 = base64.b64decode(text)
        # 使用密钥对密文进行解码
        dencoder = AES.new(self.key, self.mode)
        plain_text = dencoder.decrypt(text_base64)
        # 去除格式化中添加的非必要文本
        decoder = PKCS7Encoder()
        decrypt_text = decoder.decode(plain_text)
        return decrypt_text


if __name__ == '__main__':
    helper = AES_ENCRYPT()
    text = str(input('输入待加密文本：'))
    encrypt_text = helper.encrypt(text)
    decrypt_text = helper.unencrypt(encrypt_text)
    print '密文：', encrypt_text
    print '原文：', decrypt_text
