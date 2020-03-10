import unittest
import requests
import json
import sys

sys.path.append("../..")  # 统一将包的搜索路径提升到项目根目录下
from config.config import *
from lib.read_excel import *
from lib.case_log import Logger


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)  # 通过excel文档的路径和sheet页，已列表的方式将sheet页内的数据获取到

    def get_data_list(self, case_name):
        return get_test_data(self.data_list, case_name)  # 通过一个循环，sheet页内，匹配第一列casename值与输入的casename相等的casename的那一行值

    def send_request(self, case_data):      #这里通过传递那一行值（case_data），通过K、V 得到一行中每一列的值
        self.L = Logger()
        case_name = case_data['case_name']
        # print(case_name)
        url = case_data['url']
        method = case_data['method']
        data_type = case_data['data_type']
        headers = case_data['headers']
        args = case_data['args']
        expect_res = case_data['expect_res']
        if method.upper() == 'GET':
            res = requests.get(url=url, params=args)
            self.L.log_case_info(case_name, url, args, expect_res, res.text)
            self.assertIn(expect_res, res.text)
        elif data_type.upper() == 'FORM':
            res = requests.post(url=url, data=json.loads(args), headers=json.loads(headers))
            self.L.log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.text, expect_res)
        else:  # 注册
            res = requests.post(url=url, json=json.loads(args), headers=json.loads(headers))
            self.L.log_case_info(case_name, url, args, json.dumps(json.loads(expect_res), sort_keys=True),
                                 json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
            self.assertDictEqual(res.json(), json.loads(expect_res))
