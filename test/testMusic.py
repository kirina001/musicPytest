# -*- coding: UTF-8 -*-
from keywords.httpkeys1 import HTTP

http1 = HTTP()

# ip = '10.68.170.184:8080'
ip = '10.68.170.184:8080'

http1.post('http://'+ip+'/music_download/api/login','username=admin&password=123456')
# http1.savejson('result','id')
# http1.get('http://47.101.197.102:8080/music/api/user','{id}')

# data = {'username':'admin','password':'123456'}
# # json方式传递数据
# http1.postjson('http://47.101.197.102:8080/music/api/login',data=data)
# http1.savejson('result','id')
# http1.get('http://47.101.197.102:8080/music/api/user','{id}')

# http1.addheader('Content-type','multipart/form-data')

http1.upload('http://'+ip+'/music_download/api/song/upload','speed=0&styleId=c0a4bd86-a09b-43ac-8169-14bb69630ac0&file=G:\\music_data\\1.mp3')

# http1.upload('http://10.68.170.184:8080/music/api/song/upload','filename=1.mp3&speed=0&styleId=c0a4bd86-a09b-43ac-8169-14bb69630ac0&file1=G:/music_data/1.mp3')

