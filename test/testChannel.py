# -*- coding: UTF-8 -*-
import requests

session = requests.session()
# 登陆
# url = 'http://47.101.197.102:8080/music/api/login'
# data = {'username': 'admin', 'password': '123456'}
# result = session.post(url, data=data)
# print(result.text)

# 新增频道
# url = 'http://47.101.197.102:8080/music/api/channel'
# data = {'name': '测试频道', 'status': 2, 'type': 1}
# result = session.post(url, json=data)
# print(result.text)

# 新增专属频道
# url = 'http://47.101.197.102:8080/music/api/channel'
# data = {'name': '新增专属频道', 'status': 2, 'type': 1, 'customer': {'id': '97197731088437248'}}
# result = session.post(url, json=data)
# print(result.text)


# 编辑频道基本信息
# url = 'http://47.101.197.102:8080/music/api/channel'
# # data = {'name': '新增准数频道', 'status': '2', 'type': '2', 'customer+id': '97197731088437248'}
# data = {'name': '新增专属频道', 'status': 2, 'type': 1, 'customer': {'id': '166650120622837760'}}
#
# print(data)
# result = session.post(url, json=data)
# print(result.text)

# 为频道新增曲目
# url = 'http://47.101.197.102:8080/music/api/channel'
# song0 = {'id': '166650121226817536'}
# song1 = {'id': '166650121801437184'}
# song2 = {'id': '166650122392834048'}
# songs = [song0, song1, song2]
# data='name=新增频道曲目&status=2&type=1&id=123&songid1=111&songid2=123'
# datachannel = {'name': '频道新增曲目','status': 2, 'type': 1, 'id': '166694053419683840','songList': songs}
# print(datachannel)
# result = session.post(url, json=datachannel)
# print(result.text)

# data1 = '163758058105737216'
# data = data1.split(',')

# 获取曲目信息
# url ='http://47.101.197.102:8080/music/api/channel?filter=测试新增频道'
# result = session.get(url=url)
# print(result.text)


# 登出
# url = 'http://47.101.197.102:8080/music/api/logout'
# result = session.post(url)
# print(result.text)

# 登录
url = 'http://47.101.197.102:8080/music/api/login'
data = {'username': 'admin', 'password': '123456'}
result = session.post(url, data=data)
print(result.text)

# channelid = '170708623649935360'

#
# listsong = []
# listsong.append('id')
# listsong.append('170708624199389184')
# print(listsong)


list = {}
list['id'] = '170708624199389184'
listsong = []
listsong.append(list)




url = 'http://47.101.197.102:8080/music/api/channel/song/170708623649935360'
result = session.put(url, json=listsong)
print(result.text)
