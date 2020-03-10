import json

import requests


class Test_pj():
    url = 'http://115.28.108.130:5000/api/user/reg/'
    data = {'name': '66666g', 'password': '123456'}
    data2 = {"name": "daasw2", "password": "123456"}
    data3 = {"name": "999kkko", "password": "123456"}
    data4 = {"name": "888811s", "password": "123456"}
    str = '{"name":"222ddd1","password":"123456"}'

    # Post 传统表单提交方式
    def tradition_post(self):
        res = requests.post(url=self.url, data=self.data4)
        print(res.text)

    # Post 传递方式为json 使用字典，但是字典里面不是json格式,通过
    def post_json_json(self):
        res = requests.post(url=self.url, json=self.data)  # 字典转为字符串
        print(res.text)

    # Post 传递方式为json 使用字典，用json=str 失败  服务器无法理解请求
    def post_json_json2(self):
        res = requests.post(url=self.url, json=self.str)  # 字符串转字符串
        print(res.text)

    # 将字典转化为字符串，并声明headers  通过
    def post_json_strdata(self):
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=self.url, data=json.dumps(self.data2), headers=headers)  # data = 字符串
        print(res.text)

    # 传递字符串，并声明headers  通过
    def post_json_strdata2(self):
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=self.url, data=self.str, headers=headers)  # data = 字符串
        print(res.text)

    # 声明headers，使用data方式传递字典，失败
    def post_json_dicdata(self):
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=self.url, data=self.data3, headers=headers)  # data = 字典
        print(res.text)


T = Test_pj()
# T.post_json_json()
# T.post_json_json2()
# T.post_json_strdata2()
# T.post_json_dicdata()
T.tradition_post()
