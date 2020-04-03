import logging

# 项目路径
import os
import time
from optparse import OptionParser

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
# A = os.path.dirname(os.path.abspath('.'))
data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test', 'case','user')  # 用例目录，暂时在项目目录下
# test_path = os.path.join(prj_path, 'test')  # 用例目录，暂时在项目目录下
log_file = os.path.join(prj_path, 'log', "log_'{}'.txt".format(today))  # 也可以每天生成新的日志文件
report_file = os.path.join(prj_path, 'report', "report_'{}'.html".format(now))  # 也可以每次生成新的报告
data_file = os.path.join(data_path, 'test_user_data.xlsx')
testlist_file = os.path.join(prj_path, 'test', 'testlist.txt')
last_fails_file = os.path.join(prj_path, 'file', 'file_byte')

# log配置
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,
                    filemode='a'  # 追加模式
                    )

# 数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_password = '123456'
db = 'api_test'

# 邮件配置
send_email_after_run = False
smtp_server = 'smtp.163.com'
smtp_user = 'jiangzhe5578@163.com'
smtp_password = '1JZxnxqxx'

sender = smtp_user  # 发件人
receiver = '1045037872@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题

# 命令行选项
parser = OptionParser()

parser.add_option('--collect-only', action='store_true', dest='collect_only', help='仅列出所有用例')
parser.add_option('--rerun-fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
parser.add_option('--testlist', action='store_true', dest='testlist', help='运行test/testlist.txt列表指定用例')

parser.add_option("--testsuite=smoke_suite", action='store', dest='testsuite', help='运行指定的TestSuite')
parser.add_option("--tag=登录", action='store', dest='tag', help='运行指定tag的用例')

(options, args) = parser.parse_args()  # 应用选项（使生效）
