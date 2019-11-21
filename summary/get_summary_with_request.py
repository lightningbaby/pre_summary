#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test5.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-11-19 17:05   tangyubao      1.0         None
'''

# import lib
import requests
# ip_data='127.0.0.1'
# port_data='1087'
# new_pro={
#     'http:':'http://2001:19f0:5401:1849:5400:01ff:fee1:57c7:1234'
#   }
headers = {
    'Connection':'close',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
  }

url="https://en.wikipedia.org/api/rest_v1/page/summary/Amsterdam"
# r = requests.get(url=url,headers=headers,proxies=new_pro)
r = requests.get(url=url,headers=headers)

page = r.json()
print(page["extract"]) # Returns 'Amsterdam is the capital and...'