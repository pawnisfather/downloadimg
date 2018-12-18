#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import smtplib
import email.mime.multipart
import email.mime.text

#server = 'exmail.qq.com'
server = "smtp.exmail.qq.com"
port = '25'


def sendmail(server, port, user, pwd, msg):
    smtp = smtplib.SMTP()
    smtp.connect(server, port)
    smtp.login(user, pwd)
    smtp.sendmail(msg['from'], msg['to'], msg.as_string())
    smtp.quit()
    print('邮件发送成功email has send out !')


if __name__ == '__main__':
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = '111'
    msg['From'] = 'rd_pzl@ely.work'
    msg['To'] = '583366099@qq.com'
    user = 'rd_pzl@ely.work'
    pwd = 'wccA6525235'
    content = '%s\n%s' % ('\n'.join(sys.argv[1:4]), ' '.join(sys.argv[4:]))  # 格式处理，专门针对我们的邮件格式

    txt = email.mime.text.MIMEText(content, _charset='utf-8')
    msg.attach(txt)

    sendmail(server, port, user, pwd, msg)