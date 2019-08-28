# -*- coding: UTF-8 -*-
from keywords.httpkeys1 import HTTP
import requests,jsonpath

# http1 = HTTP()

# http1.seturl('http://47.101.197.102:8080/music/api/login')
# http1.post('http://47.101.197.102:8080/music/api/login','username=admin&password=123456')
# http1.savejson('result','id')
# http1.get('http://47.101.197.102:8080/music/api/user','{id}')


# json方式传递数据
# http1.postjson('http://47.101.197.102:8080/music/api/login', data=data)
# http1.savejson('result', 'id')
# http1.get('http://47.101.197.102:8080/music/api/user', '{id}')

# http1.upload1('http://47.101.197.102:8080/music/api/song/upload',
#               'speed=0&styleId=55956f29-a58e-47dc-a9c8-be9510c1b53c&file=F:\music_download\AlienBo.mp3')

session = requests.session()

url = 'http://10.68.170.184:8080/music_download/api/login'
data = {'username': 'admin', 'password': '123456'}
result = session.post(url, data=data)
print(result.text)

# url = 'http://10.68.170.184:8080/music/api/user/1'
# result = session.get(url)
# print(result.text)

# 上传曲目
# url = 'http://10.68.170.184:8080/music/api/song/upload'
# 此处是重点！我们操作文件上传的时候，把目标文件以open打开，然后存储到变量file里面存到一个字典里面
# file = {'file':open('G:\\music_data\\1.mp3', 'rb')}
# upload_data = {'speed':0,'styleId':'55956f29-a58e-47dc-a9c8-be9510c1b53c'}
# # 此处是重点！我们操作文件上传的时候，接口请求参数直接存到upload_data变量里面，在请求的时候，直接作为数据传递过去
# result = session.post(url=url, data=upload_data,files=file)
# print(result.text)


# 查询曲目信息
#
# url='http://10.68.170.184:8080/music/api/song?filter=1.mp3'
# result = session.get(url=url)
# print(result.text)


#
# 删除曲目
url = 'http://10.68.170.184:8080/music_download/api/song'
data1 = '163758058105737216'
data = data1.split(',')
print(data)
# data = ["163758058105737216"]
result = session.delete(url=url,json=data)
print(result.text)
