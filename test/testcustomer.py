# -*- coding: UTF-8 -*-
import requests

session = requests.session()
# 登陆
url = 'http://47.101.197.102:8080/music/api/login'
data = {'username': 'admin', 'password': '123456'}
result = session.post(url, data=data)
print(result.text)

# 新增客户
url = 'http://47.101.197.102:8080/music/api/customer'
#
# name=新增客户&tel=111&address=111&contractEnd=2019-07-25&contractStart=2019-07-25&linkMan=111
data = {'name': '新增客户', 'tel': '1111', 'address': '1', 'contractEnd': '2019-07-25', 'contractStart': '2019-07-25',
        'linkMan': '11111'}
print(data)
session.headers['Content-Type'] = 'application/json'
# session.headers['Accept']='application/json'
result = session.post(url, json=data)

print(result.text)
