# -*- coding: UTF-8 -*-
import requests

session = requests.session()
# 登陆
url = 'http://47.101.197.102:8080/music/api/login'
data = {'username': 'admin', 'password': '123456'}
result = session.post(url, data=data)
print(result.text)

url = 'http://47.101.197.102:8080/music/api/customer/167055125343375360/area/167057501689221120'
data={'box': {'id': '98528982252654592'},'customer': {'id': '167055125343375360'},'name': "新增区域"}
print(data)
result = session.put(url, json=data)
print(result.text)


# 'createTime': "2019-07-26T05:59:13.000+0000",

# 'contractEnd': '2019-07-25T00:00:00.000+0000',
# 'contractStart': '2019-07-25T00:00:00.000+0000',
# 'createTime': '2019-07-26T05:49:47.000+0000',