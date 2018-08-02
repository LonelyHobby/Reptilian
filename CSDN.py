# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:19:55 2018

@author: DELL
"""
import urllib.request
url="http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
fhandle=open("./CSDN.html","wb")
fhandle.write(data)
fhandle.close()
