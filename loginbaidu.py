# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:21:15 2018

@author: DELL
"""

import urllib.request
import urllib.parse
url="http://www.baidu.com"
name="梁军徽"
name_code=urllib.request.quote(name)
postdata=urllib.parse.urlencode({"name":"name_code","pass":"96926453wowang"}).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36')
data=urllib.request.urlopen(req).read()
fhandle=open("./loginbaidu.html","wb")
fhandle.write(data)
fhandle.close()