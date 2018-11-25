# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:57:19 2018

@author: 丁凡彧
"""

import pandas as pd
from collections import Counter
df = pd.read_csv('../data/YCL-user-poi-246w.csv')
       

df['num']=None
df=df.sort_values(by=['id','date'])


pieces = dict(list(df.groupby('id')))

ru=[]
for key in pieces:
    d=pieces[key].reset_index(drop=True)
    date1=d.loc[0,'date']
    n=0
    for i in range(d.shape[0]):
        '''
        if d.shape[0]>100:
            date2=d.loc[i,'date']
            if date2-date1 > 3:
                date1=date2
                n=n+1
        '''
        n=int(i/100)
        ru.append(key*100+n)
df['num']=ru

pieces2 = dict(list(df.groupby('num')))
name=[]
for key in pieces2:
    d=pieces2[key].reset_index(drop=True)
    d=d.drop_duplicates(['poi'])
    if d.shape[0] >=2:
        name.append(key)
df=df[df['num'].isin(name)]

values_cnt = df['num'].value_counts().index[df['num'].value_counts() > 10]
values_cnt = list(values_cnt)
df=df[df['num'].isin(values_cnt)]