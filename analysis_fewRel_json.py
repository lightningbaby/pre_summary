#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   analysis_json.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-10-31 10:53   tangyubao      1.0         None
'''

# import lib
import json
from pandas import DataFrame


def concat_whole(sent, partion_sent):
    sent = concat_sent(sent, partion_sent[0])
    sent += '< '
    sent = concat_sent(sent, partion_sent[1])
    sent += '> '
    sent = concat_sent(sent, partion_sent[2])
    sent += '< '
    sent = concat_sent(sent, partion_sent[3])
    sent += '> '
    sent = concat_sent(sent, partion_sent[4])

    return sent

def concat_whole_with_blanks(sent,partion_sent):
    sent = concat_sent(sent, partion_sent[0])
    sent += '< blank > '
    sent = concat_sent(sent, partion_sent[2])
    sent += '< blank > '
    sent = concat_sent(sent, partion_sent[4])
    return sent

def concat_sent(sent,origin_list):
    for i in origin_list:
        sent += i + ' '
    return sent

def find_pos(heads,tails):
    head1 = int(heads[2][0][0])
    head2 = int(heads[2][0][-1])
    tail1 = int(tails[2][0][0])
    tail2 = int(tails[2][0][-1])
    return [head1,head2,tail1,tail2]

def partion(pos_set,tokens):
    if(pos_set[0]>pos_set[2]):
        front=[pos_set[2],pos_set[3]]
        back=[pos_set[0],pos_set[1]]
    else:
        front=[pos_set[0],pos_set[1]]
        back=[pos_set[2],pos_set[3]]

    tokens_1=tokens[0:front[0]-1]
    tokens_2=tokens[front[0]:front[1]+1]
    tokens_3=tokens[front[1]+2:back[0]-1]
    tokens_4=tokens[back[0]:back[1]+1]
    tokens_5=tokens[back[1]+2:]

    return [tokens_1,tokens_2,tokens_3,tokens_4,tokens_5]

def get_str(ori_str):
    sent=''
    for i in ori_str:
        sent+=i +' '

    return sent
def get_entity_str(ori_str):
    sent = ''
    for i in ori_str:
        sent += i

    return sent

input_path= 'val_semeval.json'
output_path = 'train.csv'
output_blank_path='val_semeval_with_len.csv'


data=open(input_path, 'r').read()
data=json.loads(data)

corpus=[]
rel_sets=[]
for k,v in data.items():
    rel_sets.append(k)

rel_num=1
ints_num=1
for rel in rel_sets:
    for inst in data[rel]:
        tokens=inst['tokens']
        heads=inst['h']
        tails=inst['t']
        # pos_set=find_pos(heads,tails)


        # sent=''
        # partion_sent=partion(pos_set,tokens)
        # if ints_num==5126:
        #     print(pos_set)
        #     print(partion_sent)
        # sent=concat_whole(sent,partion_sent)
        # corpus.append([ints_num,rel,len(tokens),sent])
        h=get_entity_str(heads[0])
        t=get_entity_str(tails[0])
        sent=get_str(tokens)
        # sent=sent.lower()
        #
        # if h in sent and t in sent:
        #     sent=sent.replace(h,'<'+h+'>')
        #     sent=sent.replace(t,'<'+t+'>')
        # else:
        #     print(h,t)
        #     print(sent)
        corpus.append([ints_num,rel,len(tokens),h,t,sent])



        ints_num+=1
    rel_num+=1

corpus_df=DataFrame(corpus,columns=['Instance_id','Rel','Sentence_length','h','t','Sentence'])
corpus_df.to_csv(output_blank_path, index=False)


