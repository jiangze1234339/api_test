import unittest
import requests
import os
import sys
from config.config import *
from test.case.basecase import BaseCase

sys.path.append("../..")
from lib.read_excel import *
from lib.case_log import *


class TestUserLogin(BaseCase):
    # @classmethod
    # def setUp(cls) -> None:
    #     cls.list_data = excel_to_list(os.path.join(data_path, 'test_user_data.xlsx'), 'TestUserLogin')

    def test_login(self):
        """level1:正常登录"""
        all_data = self.get_data_list('test_user_login_normal')
        self.send_request(all_data)

    def test_login_wrong(self):
        wrong_data = self.get_data_list('test_user_login_password_wrong')
        self.send_request(wrong_data)
