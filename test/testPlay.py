# -*- coding: UTF-8 -*-
import requests

session = requests.session()
# 登陆
url = 'http://47.101.197.102:8080/music/api/login'
data = {'username': 'admin', 'password': '123456'}
result = session.post(url, data=data)
print(result.text)


# 新增播放计划
# url = 'http://47.101.197.102:8080/music/api/area/168104857750736896/play'
#
# data={
#
#     'area':{'id': "168104857750736896",'customer':{'id':"167138361729880064"}},
#     'channel':{'id':"167139333483008000"},
#     'endDate': "2019-07-26",
#     'endTime': "16:53",
#     'level': 3,
#     'mode': 1,
#     'startDate': "2019-07-26",
#     'startTime': "16:51"
# }
#
# print(data)
# result = session.post(url, json=data)
# print(result.text)

# area+id=168104857750736896&customer+id=167138361729880064&channel+id=167139333483008000&endDate=2019-07-26&endTime=16:53&level=3&mode=1&startDate=2019-07-26&startTime=16:51

# 编辑播放计划
url='http://47.101.197.102:8080/music/api/play/168523198931931137'

data={

    'area':{'id': "168104857750736896",'customer':{'id':"167138361729880064"}},
    'channel':{'id':"167139333483008000"},
    'endDate': "2019-07-26",
    'endTime': "22:00",
    'level': 3,
    'mode': 1,
    'startDate': "2019-07-26",
    'startTime': "12:00"
}

print(data)
result = session.put(url, json=data)
print(result.text)


