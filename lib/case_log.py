import json
from config.config import *


class Logger(object):

    def logging(self, test_name, url, data, result):
        if isinstance(data, dict):
            data = json.dumps(data, ensure_ascii=False)
        logging.info("测试用例：{}".format(test_name))
        logging.info("url：{}".format(url))
        logging.info("参数为：{}".format(data))
        logging.info("结果：{}".format(result))

    def log_case_info(self, case_name, url, args, expect_res, result):
        if isinstance(args, dict):
            data = json.dumps(args, ensure_ascii=False)
        logging.info("测试用例：{}".format(case_name))
        logging.info("url：{}".format(url))
        logging.info("参数为：{}".format(args))
        logging.info("预期结果：{}".format(expect_res))
        logging.info("结果：{}".format(result))
