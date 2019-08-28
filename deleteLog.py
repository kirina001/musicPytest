# -*- coding: UTF-8 -*-

import os

logpath = '.' + '/lib/logs/all.log'
print(logpath)
if not os.path.exists(logpath):
     pass
else:
    os.remove(logpath)


