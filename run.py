import time
import pickle
import unittest
import sys
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.mix_email import send_email
from test.case.user import test_user_available
from test.suite.test_suites import get_suite


def discover():
    return unittest.defaultTestLoader.discover(test_path)


def run(suite):
    logging.info("==============测试开始================")
    # 在路径report_file下，新建一个report.html,并在里面写入title、描述、测试人，这些通过下面这些参数写入，正文内容和附件通过.run(suite)写入,通过写好的HTMLTESTRUNNER库
    with open(report_file, 'wb') as f:
        result = HTMLTestRunner(stream=f, title='Api Test', description='测试描述', tester='姜喆').run(suite)
    if result.failures:
        save_failures(result, last_fails_file)
    if send_email_after_run:
        send_email(report_file)
    logging.info("================================== 测试结束 ==================================")


def run_all():
    run(discover())


def run_suite(suite_name):
    suite = get_suite(suite_name)
    if suite:
        run(suite)
    else:
        print('TestSuite不存在')


# 我写的，跑不起来
# def collect():  # 由于使用discover()组装的TestSuite是按文件夹目录多层嵌套的，我们把所有用例取出，放到一个无嵌套的TestSuite中，方便之后操作
#     suite = unittest.TestSuite()
#
#     def _collect(tests):
#         if isinstance(tests, unittest.TestSuite):  # 递归，如果下级元素还是TestSuite则继续往下找
#             if tests.countTestCases() != 0:
#                 for i in tests:
#                     _collect(i)
#             else:
#                 suite.addTest(tests)  # 如果下级元素是TestCase,则添加到TestSuite中
#
#     _collect(discover())
#     return suite
#
#
# def collect_only():  # 仅列出所有用例
#     t0 = time.time()
#     i = 0
#     for case in collect():
#         i += 1
#         print("{}.{}".format(str(i), case.id()))
#     print('-----------------------------------------')
#     print('Collect {} tests is {:.3f}s'.format(str(i), time.time() - t0))
# 复制的，可以
def collect():  # 由于使用discover() 组装的TestSuite是按文件夹目录多级嵌套的，我们把所有用例取出，放到一个无嵌套的TestSuite中，方便之后操作
    suite = unittest.TestSuite()

    def _collect(tests):  # 递归，如果下级元素还是TestSuite则继续往下找
        if isinstance(tests, unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)  # 如果下级元素是TestCase，则添加到TestSuite中

    _collect(discover())
    return suite


def collect_only():  # 仅列出所用用例
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i), case.id()))
    print("----------------------------------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i), time.time() - t0))


# 使用testlist.txt 运行指定case
def makesuite_by_testlist(testlist_file):
    with open(testlist_file, 'r', encoding='utf-8') as f:
        testlist = f.readlines()
    testlist = [i.strip() for i in testlist if not i.startswith("#")]  # 去掉每行结尾的"/n"和 #号开头的行
    suite = unittest.TestSuite()
    all_case = collect()
    for i in all_case:
        if i._testMethodName in testlist:
            suite.addTest(i)
    return suite


# 使用标签运行指定case
def makesuite_by_tag(tag):
    suite = unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:
            suite.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suite)


# 这个方法是为上面 run方法服务的，将失败文件方法进行封装，在run中调用此方法
def save_failures(result, last_fails_file):  # file 为序列化文件名，配置在config中
    suite = unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])  # case_result是个元祖，第一个元素是用例对象，后面是失败原因等等

    with open(last_fails_file, 'wb') as f:
        pickle.dump(suite, f)


# 当运行完run方法，将失败的case文件存放在文件中，在调用该方法进行二次运行
def return_fails():
    sys.path.append(test_path)
    with open(last_fails_file, 'rb') as f:
        suite = pickle.load(f)
    run(suite)


def main():
    if options.collect_only:  # 如果指定了--collect-only参数
        collect_only()
    elif options.rerun_fails:  # 如果指定了--rerun-fails参数
        return_fails()
    elif options.testlist:  # 如果指定了--testlist参数
        run(makesuite_by_testlist(testlist_file))
    elif options.testsuite:  # 如果指定了--testsuite=***
        run_suite(options.testsuite)
    elif options.tag:  # 如果指定了--tag=***
        run(makesuite_by_tag(options.tag))
    else:  # 否则，运行所有用例
        run_all()


suite = makesuite_by_testlist(testlist_file)
unittest.TextTestRunner().run(suite)
# if __name__ == '__main__':
#     main()  # 调用main()


# return_fails()


# makesuite_by_tag('正常登录')

# suite = makesuite_by_testlist(testlist_file)
# runner = unittest.TextTestRunner().run(suite)
# def run_all2(suite):
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
