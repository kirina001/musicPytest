# -*- coding: UTF-8 -*-
from suds.client import Client
import json
from suds.xsd.doctor import ImportDoctor, Import
from keywords.soapkeys import SOAP

# http://soap.testingedu.com/
soap = SOAP()
soap.adddoctor('')
soap.setwsdl('http://112.74.191.10:8081/inter/SOAP?wsdl')
soap.callmethod('auth')
soap.savejson('token','token')
soap.addheader('token','{token}')
soap.callmethod('login','test01、test01')
soap.callmethod('logout')





# '''
#     soap接口测试（webservice)
# '''
# # 添加默认的xmlschema
# # imp = Import('http://www.w3.ort/2001/XMLSchema', location='http://www.w3.ort/2001/XMLSchema.xsd')
# # # 添加命名空间
# # # imp.filter.add('http://soap.testingedu.com/')
# # doctor = ImportDoctor(imp)
#
# # url填写webservice的全路径
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl')
#
# # 调用auth接口
# res = client.service.auth()
# print(res)
#
# jsonResult = json.loads(res)
#
# # print(jsonResult['token'])
# header = {}
# # header['token'] = '95ebd284025d4cf1ab293300fef1fbac'
# header['token']= jsonResult['token']
#
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl', headers=header)
# param = 'test01,test01'
# param = param.split(',')
# method = 'login'
# # res = client.service.login(*param)
# # 反射调用方法
# res = client.service.__getattr__(method)(*param)
# print(res)
#
# res = client.service.logout()
# print(res)

# def test(a, b, c):
#     print(a)
#     print(b)
#     print(c)
# s = ['aa', 'bb', 'cc']
# test(*s)
