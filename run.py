# -*-coding:utf-8-*-
import time
import unittest
from package.HTMLTestRunner_cn import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


def RunTest():
    now = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
    report_path = './data/html/' + now + '.html'
    with open(report_path,"wb") as f1:
        description = '环境 ：{0} 版本：{1}'.format('安卓', '5.1')
        runner = HTMLTestRunner(stream=f1, title=u'自动化测试报告', description=description, verbosity=2)
        suite = unittest.defaultTestLoader.discover('./testcase','search*.py')
        runner.run(suite)

    send_email(report_path)


def send_email(report_path):
    """
        to_list:发给谁
        sub:主题
        content:内容
        send_mail("aaa@126.com","sub","content")
        """

    mail_host = "smtp.qq.com"
    mail_port = 465
    to_list = ['XXX@qq.com']
    mail_user = 'XXX@qq.com'
    mail_pass = 'XXX'

    with open(report_path, 'rb') as file:
        mail_body = file.read()
        me = "XXX@qq.com"
        text = MIMEText(mail_body, 'html', 'utf-8')
        msg = MIMEMultipart()
        msg.attach(text)

    msg['Subject'] = u'APP自动化测试报告'
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    try:
        s = smtplib.SMTP_SSL(mail_host, mail_port)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        print("邮件发送成功", to_list)
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    RunTest()