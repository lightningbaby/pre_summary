#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   analysis_json.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-10-30 15:58   tangyubao      1.0         None
'''

# import lib
import os
dirs = 'test2/data'
list = os.listdir(dirs)
sort_num_first=[]
for file in list:
    sort_num_first.append(int(file.split('-')[0]))
sort_num_first.sort()

# print(sort_num_first)
sorted_file = []
for sort_num in sort_num_first:
    for file in list:
        if str(sort_num) == file.split("-")[0]:
            sorted_file .append(file)
# print(sorted_file)

num=0

for l in sorted_file:
    (filename,extension) = os.path.splitext(l)
    name = filename
    file_path=dirs + '/' + l
    with open(file_path, 'r', encoding= 'utf-8') as f:
        s = f.read()
        a = ('*****'+ name + '__' + s + '\n')

    f = open('222.txt', 'a',encoding='utf-8')
    f.write(a)
    num+=1
    if num==200:
        break
# print(num)

