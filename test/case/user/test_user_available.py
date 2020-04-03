import requests

from test.case.basecase import BaseCase


class TestAvaliable(BaseCase):

    def test_get_information(self):
        all_data = self.get_data_list('test_user_avaliable')
        self.send_request(all_data)

    def test_failure_avaliable(self):
        all_data = self.get_data_list('test_failure_avaliable')
        self.send_request(all_data)

