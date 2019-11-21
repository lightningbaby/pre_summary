#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   find_weight.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-11-08 23:36   tangyubao      1.0         None
'''

# import lib
 
import csv
file_path='test_with_len.csv'
data=csv.reader(open(file_path,'r',encoding='utf-8'))
pattern='weight'

for ins in data:
    if ins[1]=='P2094':
        if str(ins[3]).find('weight')>=0:
            pass
        else:
            print(ins[3])
