from test.case.basecase import BaseCase


class TestUpdata(BaseCase):
    def test_updata(self):
        all_data = self.get_data_list('test_user_updata3')
        self.send_request(all_data)
