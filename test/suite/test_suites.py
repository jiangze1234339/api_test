import unittest

from test.case.user.test_user_login import TestUserLogin

# sys.path.append("../..")
# from test.user import test_user_login
# from test.user import test_user_reg
from test.case.user.test_user_reg import TestUserReg

smoke_suite = unittest.TestSuite()
smoke_suite.addTests([TestUserLogin('test_login'), TestUserReg('test_reg')])


def get_suite(suite_name):
    return globals().get(suite_name)

