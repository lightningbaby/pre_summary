#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_wikidata.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-11-18 10:34   tangyubao      1.0         None

pageid
ns
title
lastrevid
modified
type
id
labels  entity.attributes['labels']['en']['value'] shows the word in English
descriptions entity.attributes['descriptions']['en']['value'] descripts the word in English
aliases entity.attributes['aliases']['en'] shows all aliases,maybe some values are not in English
claims
sitelinks
'''

# import lib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from wikidata.client import Client
from wikidata.entity import Entity
client = Client()
entity = client.get('Q20145', load=True)
print(entity.attributes['descriptions']['en']['value'])
# for i,v in entity.attributes.items():
#     print(i)


# en=Entity()
# id=en.lists('IU')
# print(id)