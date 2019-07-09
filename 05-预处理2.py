# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:08:45 2019

@author: 丁凡彧
"""

import pandas as pd
df = pd.read_csv('../../data/YCL/YCL-user-poi-246w.csv')
df=df.drop_duplicates(['id','poi'])
pieces = dict(list(df.groupby('id')))
name=[]
#去除最后一个景点
drop=[]
#筛选景点数量在3-10之间的用户
for key in pieces:
    d=pieces[key]
    d=d.sort_values(by=['date','time'])
    if d.shape[0] >= 3 and d.shape[0]<=10:
        name.append(key)
        drop.append(d.tail(n=1).index.tolist()[0])
df=df[df['id'].isin(name)]
df=df[~df.index.isin(drop)]
df.to_csv('../../data/2/try(3-10)/use-poi.csv',index=False)
