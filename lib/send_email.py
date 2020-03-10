import smtplib  # 用于建立smtp连接
from email.mime.text import MIMEText

# 该模块为发送普通文字邮件的模板

# 1. 编写邮件内容（Email邮件需要专门的MIME格式）

msg = MIMEText('this is a test email', 'plain', 'utf-8')  # plain 指普通文本格式邮件内容

# 2. 组装Email头：（发件人，收件人，主题）
msg['Form'] = 'jiangzhe5578@163.com'  # 发件人
msg['To'] = '1045037872@qq.com'
msg['Subject'] = 'Api Test Report'

# 3. 连接smtp服务器并发送邮件
smtp = smtplib.SMTP_SSL('smtp.163.com')
smtp.login('jiangzhe5578@163.com', '1JZxnxqxx')
smtp.sendmail('jiangzhe5578@163.com', '1045037872@qq.com', msg.as_string())
smtp.quit()
