import json
import os
from config.config import *
import requests
import unittest
from lib.read_excel import *
from lib.interface_mysql import Mysql
from config.config import *
from test.case.basecase import BaseCase


class TestUserReg(BaseCase):
    @classmethod
    def setUp(cls) -> None:
        # cls.all_data = excel_to_list(os.path.join(data_path, 'test_user_data.xlsx'), 'TestUserReg')
        cls.mysql = Mysql()

    def test_reg(self):
        all_data = self.get_data_list('test_user_reg_normal')
        # 环境检查
        name = json.loads(all_data.get('args')).get('name')
        password = json.loads(all_data.get('args')).get('password')
        if self.mysql.check_user(name):
            self.mysql.delete(name)
        self.send_request(all_data)
        self.mysql.add(name, password)
        self.assertTrue(self.mysql.check_user(name))
        self.mysql.delete(name)

    def test_reg_exist(self):
        exist_data = self.get_data_list('test_user_reg_exist')
        self.send_request(exist_data)
