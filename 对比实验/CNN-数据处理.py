# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:51:10 2019

@author: 丁凡彧
"""

import pandas as pd  
df = pd.read_csv('../../data/2/try(3-10)/use-poi-dropt1.csv')
df=df.drop_duplicates(['id','poi'])
train_y= pd.read_csv('../../data/2/try_con/Y-train.csv',index_col=0)
test_y=pd.read_csv('../../data/2/try_con/Y-test.csv',index_col=0)
test_x=df[df['id'].isin(test_y.index)]
train_x=df[df['id'].isin(train_y.index)]

pieces = dict(list(train_x.groupby('id')))
Du_train=[]
key_train=[]
for key in pieces:
    d=pieces[key]
    d_poi=d['poi'].tolist()
    
    for i in range(9-len(d_poi)):
        d_poi.append(0.0)
    Du_train.append(d_poi)
    key_train.append(key)
train=pd.DataFrame(Du_train,index=key_train)
pieces = dict(list(test_x.groupby('id')))
Du_test=[]
key_test=[]
for key in pieces:
    d=pieces[key]
    d_poi=d['poi'].tolist()
    
    for i in range(9-len(d_poi)):
        d_poi.append(0.0)
    Du_test.append(d_poi)
    key_test.append(key)
test=pd.DataFrame(Du_test,index=key_test)
train.to_csv('../../data/2/try_cnn/TX-train.csv')
test.to_csv('../../data/2/try_cnn/TX-test.csv')