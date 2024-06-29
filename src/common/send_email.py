import smtplib
from email.mime.text import MIMEText
from email.header import Header
from src.common.log_utils import LogUtils

"""
    实现思路：
    1、设置第三方代理商的服务区
    2、获取该第三方代理商账号与授权码
    3、设置发件人与收件人
    4、编写邮件标题与正文内容
    5、与第三方服务器建立连接
    6、登入第三方个人账号
    7、使用第三方发送邮件
    8、与第三方服务器断开连接
"""


class SendEmail:
    lu = LogUtils().get_log()

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_port = 465

    mail_user = ""  # 用户名
    mail_pass = ""  # 口令

    sender = ''
    receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('正文内容', 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = ','.join(receivers)

    subject = ''
    message['Subject'] = Header(subject, 'utf-8')

    try:
        # 创建一个 SMTP_SSL 对象并连接到服务器
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        lu.info("邮件发送成功")
        quit = smtpObj.quit()
        lu.info(quit)
    except smtplib.SMTPException as e:
        lu.info("Error: 无法发送邮件:", e)

