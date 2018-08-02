# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:41:03 2018

@author: DELL
"""

import urllib.request
keywd="hello"
url="https://www.baidu.com/s?word="+keywd+"&tn=99621802_hao_pg&ie=utf-8&sc=UWY4rHmznH6sn-qCmyqxTAThIjYkPHn1nHbYPW64rjcsFhnqpA7EnHc1Fh7W5Hm4njT4P1Tkr0&ssl_sample=s_4%2Cs_10%2Cs_76&srcqid=2264041778607784738"
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open("./hellobaidu.html","wb")
fhandle.write(data)
fhandle.close()