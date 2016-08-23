import unittest,time,os,smtplib
#from smtplib import SMTP 
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# ================定义发送邮件===============

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    
    smtpserver = 'smtp.sina.com'
    sender = 'galibang_001@sina.com'
    receiver = '1968304695@qq.com'
    user = 'galibang_001@sina.com'
    password = 'galibang001'
    
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("Auto-test Report", 'utf-8')
    
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    
    print('email has been sent')

# ==查找测试报告目录，找到最新生成的测试报告文件==

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "\\" +fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    
    test_dir = 'D:\\Python35\\MyPython\\test_case'
    test_report = 'D:\\Python35\\MyPython\\report'
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern = 'test_*.py')

    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = test_report+ '\\' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = '测试报告',
                            description = '用例执行情况：')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)
