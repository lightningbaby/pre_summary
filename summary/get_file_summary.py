#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test7.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-11-20 15:57   tangyubao      1.0         None
'''

# import lib
import numpy as np
import wikipedia
NOT_FOUND_LIST=[]
DisE=wikipedia.exceptions.DisambiguationError
PagE=wikipedia.exceptions.PageError
def get_summary(words_list,words_summary):
    temp=''
    for w in words_list:
        try:
            temp=wikipedia.summary(w,sentences=2)
        except wikipedia.exceptions.DisambiguationError as DisambiguationE:
            first_word=DisambiguationE.options[0]
            if first_word != None:
                temp=wikipedia.summary(first_word,sentences=2)

            else:
                NOT_FOUND_WORD =NOT_FOUND_WORD+1
                temp='None'
                NOT_FOUND_LIST.append(w)
        except wikipedia.exceptions.PageError as PageE:
            print(PageE)
            temp='None'
            NOT_FOUND_LIST.append(w)

        words_summary.append(temp)
    return words_summary

def get_summary2(words_list,words_summary,NOT_FOUND_WORD):
    temp=''
    for w in words_list:
        try:
            temp=wikipedia.summary(w,sentences=2)
        except wikipedia.exceptions as e:
            temp = 'None'
            NOT_FOUND_LIST.append(w)
            NOT_FOUND_WORD =NOT_FOUND_WORD +1

    return words_summary,NOT_FOUND_WORD

def save_summary(file_name,words_summary):
    temp=np.array(words_summary)
    np.save(file_name,temp)

def find_word(word,words_list):
    if word not in words_list:
        print(word,' not in list')

heads=np.load('heads.npy').tolist()
tails=np.load('tails.npy').tolist()

# find_word('tour de airfiel',heads)
# find_word('tour de airfiel',tails)


wikipedia.set_lang('en')
heads_summary=[]
tails_summary=[]
HEAD_NOT_FOUND_WORD=0
TAIL_NOT_FOUND_WORD=0
heads_summary,HEAD_NOT_FOUND_WORD=get_summary2(heads,heads_summary,HEAD_NOT_FOUND_WORD)
tails_summary,TAIL_NOT_FOUND_WORD=get_summary2(tails,tails_summary,TAIL_NOT_FOUND_WORD)

save_summary('heads_summary.npy',heads_summary)
save_summary('tails_summary.npy',tails_summary)
print(HEAD_NOT_FOUND_WORD,TAIL_NOT_FOUND_WORD)
print(NOT_FOUND_LIST)