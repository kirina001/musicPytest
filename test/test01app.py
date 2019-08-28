# -*- coding: UTF-8 -*-

conf = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.FreshAir",
    "appActivity": ".activity.WelcomeActivity",
    "noReset": "true",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true"
}

c = eval(str(conf))
print(type(c))
