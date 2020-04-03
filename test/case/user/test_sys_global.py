from test.case.basecase import BaseCase


class Test_Sui_city(BaseCase):

    def test_sui_city(self):
        all_data = self.get_data_list('test_sui_data1')
        self.send_request(all_data)