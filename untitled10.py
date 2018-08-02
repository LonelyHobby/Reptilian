# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:11:18 2018

@author: DELL
"""

import urllib.request
file=urllib.request.urlopen("http://www.baidu.com")
data=file.read()
dataline=file.readline()
'''
print(dataline)
print(data)
'''
fhandle=open("./baidu.html","wb")
fhandle.write(data)
fhandle.close()