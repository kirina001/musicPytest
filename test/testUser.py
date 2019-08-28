# -*- coding: UTF-8 -*-
import requests

session = requests.session()
# 登陆
url = 'http://47.101.197.102:8080/music/api/login'
data = {'username': 'admin', 'password': '123456'}
result = session.post(url, data=data)
print(result.text)

# 新增用户
# url = 'http://10.68.170.184:8080/music/api/user'
# data = {'username': "新增1",'nickName': "aa1",'password': "cc123456",'phone': "18055555555",'role': {'id': '1'}}
# result = session.post(url, json=data)
# print(result.text)

# 新账号登录
# session.headers.clear()
# url = 'http://10.68.170.184:8080/music/api/login'
# data = {'username': '新增1', 'password': 'cc123456'}
# result = session.post(url, data=data)
# print(result.text)

# # 查询id
# url='http://10.68.170.184:8080/music/api/user?pageNum=1&pageSize=10&currentPage=1&totalSize=2&filter=aa1'
# result = session.get(url)
# print(result.text)
# id='171424810193129472'

# 编辑用户
url = 'http://47.101.197.102:8080/music/api/user/171736116989267968'

# data1 = {'username': "a333",'nickName': "aa1",'password': "$2a$10$kxZKil2zlau7n6FTiTVFquk2gbtp7YBPVn8vico.h6jBIZiDt.CxG",'phone': "18055555555",'role': {'id': '1'}}

# data={'createBy': "1",
# 'id': "171736116989267968",
# 'nickName': "新增",
# 'password': "$2a$10$nGYWoTtCWYLPNQzsH5ItKOqFvUIF67i6U8U9qW1lOo8xRqErwM5fq",
# 'phone': "18011111111",
# 'status': 0,
# 'updateBy': "1",
# 'username': "ad2",
# 'role':{'id':'1'}
# }

data={
'nickName': "新增",'password': "cc111",'status': 0,'username': "ad6",'role':{'id':'1'}}
# 'phone': "18011111111",


result = session.put(url, json=data)
print(result.text)






# 编辑用户登录
# url = 'http://10.68.170.184:8080/music/api/login'
# data = {'username': 'a222', 'password': 'cc123456'}
# result = session.post(url, data=data)
# print(result.text)

# 登出
# url='http://10.68.170.184:8080/music/api/logout'
# result = session.post(url)
# print(result.text)




# 存在问题
# 1.新增用户可以登录
# 2.修改用户名之后无法登录
#