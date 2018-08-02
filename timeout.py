# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:34:40 2018

@author: DELL
"""

import urllib.request
for i in range(1,50):
    try:
        file=urllib.request.urlopen("http://www.baidu.com",timeout=1)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("出现异常"+str(e))