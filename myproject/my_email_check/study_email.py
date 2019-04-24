# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import random


def get_random_str(length):
    result_num = ""
    for i in range(length):
        result_num += str(int(random.random() * 10))
    return result_num


def mail():
    '''

    :return:
    '''
    my_sender = '965634203@qq.com'  # 发件人邮箱账号
    my_pass = 'ymbhrnahoabnbehf'  # 发件人邮箱密码
    my_user = '209364619@qq.com'  # 收件人邮箱账号，我这边发送给自己

    ret = True
    try:
        code = get_random_str(6)
        msg = MIMEText('邮件的主体内容，例如生成的验证码:' + code, 'plain', 'utf-8')
        msg['From'] = formataddr(["HPH", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["你是我的小号", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "HPH 测试邮件"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret, code


if __name__ == '__main__':
    ret, code = mail()
    if ret:
        print("邮件发送成功！验证码：" + code)
    else:
        print("邮件发送失败")
