# -*- coding: UTF-8 -*-
from keywords.webkeys import Web


web = Web(0000)


# 浏览器分辨率应该设置为100%显示
driver = web.openbrowser('ff','./lib/tools/','10')
# web.sleep(5)
# web.openurl('http://10.68.170.184:8080/music/#/login?redirect=%2Fdashboard')
# # web.sleep(5)
# web.inputtext("//input[@name='username']","admin")
# # web.sleep(5)
# web.inputtext("//input[@placeholder='password']","123456")
# # web.sleep(5)
# web.click("//button[@class='el-button el-button--primary']")