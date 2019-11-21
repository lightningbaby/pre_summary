#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test4.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-11-19 15:21   tangyubao      1.0         None
'''

# import lib
import wikipedia
# try:
#     mercury = wikipedia.summary("IU")
# except wikipedia.exceptions.DisambiguationError as e:
#     print(e.options)

# print(wikipedia.summary('IU',sentences=2))
wikipedia.set_lang('en')
# words_list=['IU','Smita Patil','Raj Babbar','Krishna','Rukmini']
words_list=['davenport municipal airport']
# descrip=[]
# for w in words_list:
#     # descrip.append(wikipedia.summary(w,sentences=2))
#     try:
#         mercury = wikipedia.summary(w,sentences=2)
#     except wikipedia.exceptions.DisambiguationError as e:
#         print(e.options)
#         w=wikipedia.suggest(w)
#         mercury = wikipedia.summary(w, sentences=2)
#     descrip.append(mercury)
# print(descrip)
# print(wikipedia.suggest('IU'))
# print(wikipedia.summary('davenport municipal airport'))
try:
    print(wikipedia.summary('IU'))
except wikipedia.exceptions.DisambiguationError as e:
    # print(e.options)
    # opt=e.options
    # print(opt[0])
    print(wikipedia.summary(e.options[0]))
