# -*- coding: UTF-8 -*-
import requests, json, jsonpath

session = requests.session()

url = 'http://10.68.170.184:8080/music_download/api/login'
data = {'username': 'admin', 'password': '123456'}
response = session.post(url, data=data)
print(response.text)
userid = json.loads(response.text)['result']
# print(userid)

url = 'http://10.68.170.184:8080/music_download/api/user/1'
response = session.get(url)
print(response.text)

url = 'http://10.68.170.184:8080/music_download/api/logout'
response = session.get(url)
print(response.text)





# url = 'http://47.100.254.37:8888/freshair-server/api/manage/login'

# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# headers = {
#      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
