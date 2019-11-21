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
import csv
dirs = 'test2/data'
list = os.listdir(dirs)
sort_num_first=[]
for file in list:
    sort_num_first.append(int(file.split('-')[0]))
sort_num_first.sort()

sorted_file = []
for sort_num in sort_num_first:
    for file in list:
        if str(sort_num) == file.split("-")[0]:
            sorted_file .append(file)

num=0

for l in sorted_file:
    (filename,extension) = os.path.splitext(l)
    name = filename
    file_path=dirs + '/' + l
    file_words=[]
    csv_file=csv.reader(open(file_path,'r',encoding='gbk'))
    for w in csv_file:
        file_words.append(w)
    a = '*****'+ name + '__'+str(file_words)
    f = open('222.txt', 'a',encoding='gbk')
    f.writelines(a)
    # num+=1
    # if num==200:
    #     break
