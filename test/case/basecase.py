import unittest
import requests
import json
import sys

sys.path.append("../..")  # 统一将包的搜索路径提升到项目根目录下
from config.config import *
from lib.read_excel import *
from lib.case_log import Logger
from lib.interface_mysql import Mysql


class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()
        url = 'http://115.28.108.130:5000/api/user/login/'
        data = {'name': '张三', 'password': '123456'}
        cls.session.post(url=url, data=data)
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)  # 通过excel文档的路径和sheet页，已列表的方式将sheet页内的数据获取到

    def get_data_list(self, case_name):
        return get_test_data(self.data_list, case_name)  # 通过一个循环，sheet页内，匹配第一列casename值与输入的casename相等的casename的那一行值

    def send_request(self, case_data):  # 这里通过传递那一行值（case_data），通过K、V 得到一行中每一列的值
        self.flag = False
        self.L = Logger()
        case_name = case_data['case_name']
        # print(case_name)
        url = case_data['url']
        method = case_data['method']
        data_type = case_data['data_type']
        headers = case_data['headers']
        args = case_data['args']
        expect_res = case_data['expect_res']
        # 此处的方法是将写在用例中的SQL语句，通过mysql执行，执行后进行处理得到结果再与从接口中得到的数据进行比对
        mysql = Mysql()
        # 调用mysql中封装好的查询方法，传入写在用例中的sql
        sql_result = mysql.select_test(expect_res)
        # 得到sql的结果是一个元组，（（A，xxxx））
        single_result = sql_result[0]
        # 进行一步步剥皮，最后得到xxx
        final_result = int(single_result[0])
        if method.upper() == 'GET':
            # 1.如果后面的接口都需要保持登录状态，则，使用下面这行注释
            #   res = self.session.get(url=url, params=args)
            # 2.下面三行是验证get方式请求页面是否成功，
            # res = requests.get(url=url, params=args)
            # self.L.log_case_info(case_name, url, args, expect_res, res.text)
            # self.assertIn(expect_res, res.text)
            # 3. 这个是验证请求的数据
            res = requests.get(url=url)
            all_dic = res.json()
            data_dic = all_dic['data']
            self.L.log_case_info(case_name, url, args, expect_res, data_dic)
            if data_type == 'sex':
                list_age = data_dic['age']
                for i in list_age:
                    if final_result == i['value']:
                        self.flag = True
                        break
            try:
                self.assertTrue(self.flag)
                print('{} Pass'.format(case_name))
            except Exception as e:
                print('{}:测试失败'.format(case_name))

        elif data_type.upper() == 'FORM':
            res = requests.post(url=url, data=json.loads(args), headers=json.loads(headers))
            self.L.log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.text, expect_res)
        else:  # 注册
            res = requests.post(url=url, json=json.loads(args), headers=json.loads(headers))
            self.L.log_case_info(case_name, url, args, json.dumps(json.loads(expect_res), sort_keys=True),
                                 json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
            self.assertDictEqual(res.json(), json.loads(expect_res))
