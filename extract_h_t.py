#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test6.py    
@Contact :   lightningtyb@163.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-11-20 15:41   tangyubao      1.0         None
'''

# import lib
 
import csv
import pandas as pd
import numpy as np
file_path='train_with_len.csv'
# data=csv.reader(open(file_path,'r',encoding='utf-8'))
# heads=data['h']
# tails=data['t']

data=pd.read_csv(file_path)
heads=data['h']
tails=data['t']
heads=np.array(heads)
tails=np.array(tails)

np.save('heads.npy',heads)
np.save('tails.npy',tails)