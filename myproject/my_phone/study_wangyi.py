# coding=utf-8
import hashlib
import time
import uuid
import requests

'''
    基于网易云信
    注册获取20条测试短信，目测是restful，可以通过curl直接进行操作。
'''
if __name__ == '__main__':
    #
    sms_url = 'https://api.netease.im/sms/sendcode.action'
    post_data = {
        'mobile': '17712153637'

    }

    cur_time = str(time.time())
    app_secret = 'bd0946fa9e05'
    nonce = str(uuid.uuid4())

    # 参数拼接
    before = app_secret + nonce + cur_time
    # 哈希加密
    # 进行SHA1哈希计算，转化成16进制字符(String，小写)
    check_sum = hashlib.new('sha1', before.encode('utf-8')).hexdigest()

    headers = {
        'AppKey': '9d5359f128af72a3872b82abc6866542',  # 开发者平台分配的appkey
        'Nonce': nonce,
        'CurTime': cur_time,
        'CheckSum': check_sum
    }

    response = requests.post(sms_url, data=post_data, headers=headers)
    # 返回json字符串
    # msg字段表示此次发送的sendid；obj字段表示此次发送的验证码。
    print(response.json())
