import requests
# 导入requests_toolbelt库使用MultipartEncoder
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests

session = requests.session()

session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
session.headers['Content-type'] = 'application/x-www-form-urlencoded'
session.headers['Accept'] = 'application/json'

url = 'http://10.68.170.184:8080/music_download/api/login'
result = session.post(url, 'username=admin&password=123456')
res = result.text
print(res)
# 获取用户信息
url = 'http://10.68.170.184:8080/music_download/api/user/1'
result = session.get(url)
res = result.text
print(res)

url = 'http://10.68.170.184:8080/music_download/api/song/upload'
# # 上传文件
path = 'G:\\music_data\\aa.mp3'
mm = MultipartEncoder(
    fields={'speed': '1',
            'styleId': 'c0a4bd86-a09b-43ac-8169-14bb69630ac0',
            'file': ('file', open(path, 'rb'))},
)
ss = mm.boundary
# print(ss)
# print('生成Content-Type' + str(mm.content_type))
# session.headers['Content-Type'] = mm.content_type
# result = session.post(url=url, data=mm)
# res = result.text
# print(result.status_code)
# print(res)


# 调试数据
session.headers['Content-Type'] = 'multipart/form-data; boundary='+ss+''

print(session.headers['Content-Type'])

result = session.post(url=url, data=mm)
res = result.text
print(result.status_code)
print(res)




# session.headers['Content-type'] = 'multipart/form-data'
# url = 'http://10.68.170.184:8080/music/api/song/upload'
#
# file = {
#     'file': open('G:\\music_data\\aa.mp3', 'rb','audio/mp3')
# }
# print(file.__sizeof__())
#
# data = {
#     'speed': 1,
#     'styleId': 'c0a4bd86-a09b-43ac-8169-14bb69630ac0',
#     'notes': '备注'
# }
