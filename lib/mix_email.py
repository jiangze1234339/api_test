import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from config.config import *


# 该模块为发送带有html附件的模板

def send_email(report_file):
    # 定义邮件的格式及元素
    msg = MIMEMultipart()  # 混合MIME格式 简单说就是这个邮箱里面可以有多种元素
    # 这行文字，是通过msg.attach ，向邮件正文添加正文，正文就是："MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8')"
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）
    # 邮件头内容
    msg['Form'] = 'jiangzhe5578@163.com'  # 发件人
    msg['To'] = '1045037872@qq.com'  # 收件人
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件头标题
    # 添加附件模块
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'  # 设置上传方式
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    # 这里就是将写好的附件模块，att1,通过msg.attach添加到邮件附件中      msg是个主题，MiMEText和att1 分别是正文和附件，并添加到msg上面
    msg.attach(att1)
    # 发送操作
    try:
        smtp = smtplib.SMTP_SSL(smtp_server)  # smtp代理地址 负责转发
        smtp.login(smtp_user, smtp_password)  # 这个是发件人的邮箱密码
        smtp.sendmail(sender, receiver, msg.as_string())  # 依次为发件人，收件人、以及内容
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
