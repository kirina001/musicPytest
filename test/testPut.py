# -*- coding: UTF-8 -*-
from keywords.httpkeys1 import HTTP
import requests

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

# 登陆
url = 'http://47.101.197.102:8080/music/api/login'
data = {'username': 'admin', 'password': '123456'}
result = session.post(url, data=data)
# print(session.cookies)
print(result.cookies.values())
print(result.text)


# 清空session
# session.__init__()


# 获取用户信息
# url = 'http://47.101.197.102:8080/music/api/user/1'
# # print(session.cookies)
# result = session.get(url)
# print(result.text)

# 上传曲目信息
# url = 'http://47.101.197.102:8080/music/api/song/upload'
# 此处是重点！我们操作文件上传的时候，把目标文件以open打开，然后存储到变量file里面存到一个字典里面
# file = {'file':open('F:\\music_download\\AlienBo.mp3', 'rb')}
# upload_data = {'speed':0,'styleId':'55956f29-a58e-47dc-a9c8-be9510c1b53c'}
# # 此处是重点！我们操作文件上传的时候，接口请求参数直接存到upload_data变量里面，在请求的时候，直接作为数据传递过去
# result = session.post(url=url, data=upload_data,files=file)
# print(result.text)


# 下载曲目并保存到本地
# url = 'http://47.101.197.102:8080/music/api/song/download/148744925880520704'
# result = session.get(url=url, stream=True)
# print(result.status_code)

# 处理服务器返回的数据
# filename = './lib/music_download/aa.mp3'
#
# with open(filename, "wb") as f:
#     for chunk in result.iter_content(chunk_size=512):
#         f.write(chunk)
#     print('下载完毕')


# 播放曲目
url = 'http://47.101.197.102:8080/music/api/song/play/148744925880520704'
result = session.get(url=url)
print(result.status_code)
print(result.text)

# 删除曲目
# url ='http://47.101.197.102:8080/music/api/song/download'
# path='190603010256'
# url=url+'/'+path
# result = session.get(url=url)
# print(result.text)

# 编辑曲目信息
# url = 'http://47.101.197.102:8080/music/api/song/164454249369964544'
# data ={"author": "测试表演","name": "aa.mp3","speed": 0,"style": {"id": '2'}}
#
# ss = 'author=测试表演&name=AlienBo.mp3&speed=0&style+Id=2'
# # 对数据进行组装
# str1 = {'author': '测试表演', 'name': 'aa.mp3', 'speed': '0', 'style': {'id': '2'}}
# print(type(data))
# session.headers['Content-Type'] = 'application/json'
# result = session.put(url=url, json=str1)
# print(result.text)

# 登出
# url = 'http://47.101.197.102:8080/music/api/logout'
# result = session.post(url=url,data=None,cookies=None)
#
# print(result.text)
# print(session.cookies)


# 清除cookie中的jsessionid
# cookies = requests.utils.dict_from_cookiejar(session.cookies)
# print('cookies: ', cookies)
# # 结果:
# # cookies:  {}

# cook1 = {'JSESSIONID': ''}
# # requests.utils.cookiejar_from_dict方法可以将一个字典转换成cookiejar对象并添加到当前session的cookies中
# session.cookies = requests.utils.cookiejar_from_dict(cook1)
# cookies = requests.utils.dict_from_cookiejar(session.cookies)
# print('cookies: ', cookies)
