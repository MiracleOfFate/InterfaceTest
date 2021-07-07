import smtplib
from email.mime.text import MIMEText


class sendmail:
    def send_mail(self, path):
        f = open(path, 'rb')
        mail_body = f.read()
        f.close()

        host = 'smtp.qq.com'
        # port = 25
        # host = 'smtp.163.com'
        port = 465
        # sender = 'daniel_402@163.com'  # 发送者邮箱地址
        # pwd = "HTHNHAWSEFUYCCGX"  # 授权码，不是邮箱登录密码
        sender = '2621692424@qq.com'  # 发送者邮箱地址
        pwd = "kcnpgguhzbaldijg"  # 授权码，不是邮箱登录密码
        receiver = "2621692424@qq.com"  # 接收者邮箱地址

        msg = MIMEText(mail_body, 'HTML', 'UTF-8')
        msg['subject'] = "api测试报告发送"    # 设置邮件主题
        msg['from'] = sender                # 发送方信息
        msg['to'] = receiver                # 接收方信息

        # 通过SSL方式发送，服务器地址和端口
        s = smtplib.SMTP_SSL(host, port)
        # s = smtplib.SMTP()
        # s.connect(host, port)
        # 登录邮箱
        s.login(sender, pwd)

        # 开始发送
        s.sendmail(sender, receiver, msg.as_string())


# import smtplib
# from email.mime.text import MIMEText
#
# # 登陆邮箱
# sent=smtplib.SMTP()
# sent.connect('smtp.qq.com',25)
# mail_name="2621692424@qq.com" # 发送人邮箱地址
# mail_password = "kcnpgguhzbaldijg" # 注意：这里不是密码，而应该填写授权码！！
# sent.login(mail_name, mail_password) # 登陆
#
# # 编辑邮件内容
# to = ['2621692424@qq.com'] # 收件人邮箱地址
# content = MIMEText('你好，我是圣洁不吃冰淇淋🍦') # 正文内容
# content['Subject'] = '漂流瓶' # 邮件标题
# content['From'] = mail_name # 发件人
# content['To'] =','.join(to) #收件人，用逗号连接多个邮件，实现群发
#
# # 发送邮件
# try:
#     sent.sendmail(mail_name, to, content.as_string())  #3个参数 发送人，收件人，邮件内容
#     print('Success')
#     sent.close()
# except smtplib.SMTPException:
#     print("Error：Fail")
