import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

'''
#发送邮箱服务器
smtpserver = 'smtp.sina.com'

#发送邮箱
sender = 'galibang_001@sina.com'

#接收邮箱
receiver = '1968304695@qq.com'

#发送邮箱用户/密码
user = 'galibang_001@sina.com'
password = 'galibang001'
'''
subject = 'Python send mail test'

sendfile = open('D:\\Python35\\README.txt','rb').read()

att = MIMEText(sendfile,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="README.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)
'''
#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()
'''
smtp = smtplib.SMTP()
smtp.connect('smtp.sina.com')
smtp.login('galibang_001@sina.com','galibang001')
smtp.sendmail('galibang_001@sina.com','1968304695@qq.com',msgRoot.as_string())
smtp.quit()
