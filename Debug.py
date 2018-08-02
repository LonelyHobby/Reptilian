# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:50:31 2018

@author: DELL
"""

import urllib.request
httphd=urllib.request.HTTPHandler(debuglevel=1)
httpshd=urllib.request.HTTPSHandler(debuglevel=1)
opener=urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data=urllib.request.urlopen("http://edu.51cto.com")
