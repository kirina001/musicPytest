# -*- coding: UTF-8 -*-
import os, time, threading
from keywords.appkeys import APP

'''
    test5
'''
app = APP(None)
app.runappium('C:\\Program Files (x86)\\Appium', '4723', 10)
# conf = {
#     "platformName": "Android",
#     "platformVersion": "6.0.1",
#     "deviceName": "127.0.0.1:7555",
#     "appPackage": "com.FreshAir",
#     "appActivity": ".activity.WelcomeActivity",
#     "noReset": "true",
#     "unicodeKeyboard": "true",
#     "resetKeyboard": "true"
# }
# conf = str(conf)

app.runapp('{"platformName": "Android","platformVersion": "6.0.1","deviceName": "127.0.0.1:7555","appPackage": "com.FreshAir","appActivity": ".activity.WelcomeActivity","noReset": "true","unicodeKeyboard": "true","resetKeyboard": "true"}',10)
'''
    test1
'''
# os.system('node \"C:\\Program Files (x86)\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js\"')
# os.system('appium -a 127.0.0.1 -p 4723')

'''
    test2
'''
# def run(cmd):
#     res = os.system(cmd)
#     print('子线程')
#     return res
#
# # 待执行cmd命令
# appium = 'node \"C:\\Program Files (x86)\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js\"'
# # 创建线程
# th = threading.Thread(target=run, args=(appium,))
# # 执行线程
# th.start()
# print('主线程')

# help(threading.Thread)


'''
    test3
'''
# process = os.popen("netstat -aon |findstr 4723").read()
# pid = process.replace('  ', '').split(" ")[2]
# print(pid)
# m = os.popen("taskkill -f -pid %s" % pid)
# print(m.read())
# print('appium服务关闭完毕')

'''
    test4
'''
# 常用命令
# ip = os.system('ipconfig')
# dir = os.system('dir')
# cd = os.system('cd')
