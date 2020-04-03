import json
import unittest

import requests

from test.case.basecase import BaseCase


class Test_Sui_city(BaseCase):

    def test_sui_city(self):
        i = 0
        while i < 3:
            i += 1
            all_data = self.get_data_list('test_sui_data{}'.format(i))
            self.send_request(all_data)

    # def test(self):
    #     case_name = 'test_sui_data1'
    #     all_data = self.get_data_list(case_name)
    #     self.send_request(all_data)

# url = 'http://10.7.24.178:15000/api/yg/home/page'
# res = requests.get(url=url)
#
# dic = res.json()
# D = (dic['data'])
# chart = D['sex']
# man = chart[0]
# boy_data = man['value']
# women = chart[2]
# girl_data = women['value']
# print(boy_data, girl_data)
