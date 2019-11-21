#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test3.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-11-19 14:06   tangyubao      1.0         None
'''

# import lib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from wikidata.client import Client
from wikidata.entity import Entity
import requests
params = dict (
        action='wbsearchentities',
        format='json',
        language='en',
        uselang='en',
        search='Smita Patil'
        )

response = requests.get('https://www.wikidata.org/w/api.php?', params).json()
# id=response.get('search')[0]['id']
ret=response.get('search')
# print(ret)
# for i in ret:
#     print(i['label'])
#     print(i['description'])
for k in ret:
    print(k.keys())
# client = Client()
# entity = client.get(id, load=True)
# print(entity)
# print(entity.attributes['descriptions']['en']['value'])
