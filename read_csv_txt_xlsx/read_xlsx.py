#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   read_xlsx.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-11-11 11:23   tangyubao      1.0         None
'''

# import lib
 

import pandas as pd

inputfile_1 = "ha.xlsx"

data1 = pd.read_excel(inputfile_1)#,index_col = '序号'

#打印表头
# list1 = data1.columns
#
# print(list1)
i=0
father=0
for data in data1.values:
    if '哈哈哈哈哈哈哈' in str(data):
        pass
    elif 'concubine' in str(data).lower():
        father+=1
    # if 'widow' in str(data).lower():
    #     father += 1
    else:
        print(data)
        i+=1
print(i)
print(father)