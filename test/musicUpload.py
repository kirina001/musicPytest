
# 上传文件时需要的参数列表
data = {
    'username': 'admin',
    'password': '123456'
}
# 文件列表
files = {}

res = session.post('http://47.101.197.102:8080/music_download/api/login', data=data)
response = res.content.decode(res.apparent_encoding)
print(response)

# open('C:\\Users\\Will\\Desktop\\林子祥 - 男儿当自强(1).mp3', 'rb').read()

session.headers['Content-Length'] = '4230950'
session.headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundary7xiZYpamWXV9ZHgt'

d = {
    'file': ('林子祥 - 男儿当自强(1).mp3',open('C:\\Users\\Will\\Desktop\\林子祥 - 男儿当自强(1).mp3', 'rb')),
    'speed': (None,'1'),
    'styleId': (None,'2db2a093-a164-4c90-9d76-5db90ba49764'),
    'notes': (None,'')
}
res = session.post('http://47.101.197.102:8080/music_download/api/song/upload',files=d)
response = res.content.decode(res.apparent_encoding)
# print(res.request.body)
print(response)