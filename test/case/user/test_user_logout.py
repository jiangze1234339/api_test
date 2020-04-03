from test.case.basecase import *


class TestLogout(BaseCase):  # 这里直接继承BaseCase
    def test_user_logout(self):
        # """level1:正常退出"""
        case_data = self.get_data_list("test_user_logout")
        self.send_request(case_data)



