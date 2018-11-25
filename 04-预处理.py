# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:36:04 2018

@author: 丁凡彧
"""

import pandas as pd
from collections import Counter

df = pd.read_csv('../data/use-poi127-900w.csv')
df.columns=['date','time','id','lng','lat','poi','loc'] 
useri = pd.read_csv('../data/alluser-i.csv')
useri.columns=['id', 0,1,2,3,4,5,6,7,8,9]
userid=list(useri['id'])
#用户坐标与用户标签求交集，删除没有用户标签的用户
df=df[df['id'].isin(userid)]
#排除跟踪记录少于5的用户
values_cnt = df['id'].value_counts().index[df['id'].value_counts() > 5]
values_cnt = list(values_cnt)
df=df[df['id'].isin(values_cnt)]
#记得更新用户id集
#df=df.dropna(axis=0)#去空值

pieces = dict(list(df.groupby('id')))
name=[]

for key in pieces:
    d=pieces[key].reset_index(drop=True)
#去除在同一地点
    if d.drop_duplicates(['poi']).shape[0] < 2:
        d=d.drop_duplicates(['poi'])
        name.append(key)
#居住地点
    else:
#晚上八点到早上7点出现次数最多的地方是家/旅馆
        h=d[(d["time"]< 7 ) | (d["time"] > 20) ]
#如果能确定居住地再判断是否有工作地点
        home=None
        if h.shape[0] != 0:
            word_counts = Counter(h['loc'])
            home=word_counts.most_common(1)[0][0]
        #工作时间段（8~20）出现在非居住的地方5次以上即为工作
        d = d[(d["time"]> 7 ) & (d["time"] < 20) ]
        #白天没有轨迹的删除
        if d.shape[0] == 0 :
            name.append(key)
        else:
            #统计用户每天出现地方
            day=d.drop_duplicates(['date']).shape[0]
            d = d.drop_duplicates(['date','loc'])
            loc_counts = Counter(d['loc'])
            #寻找出现次数最多的非居住地和出现频率
            maxn=loc_counts.most_common(1)[0][0]
            locn=loc_counts.most_common(1)[0][1]
            if maxn == home:
                if len(loc_counts) == 1:
                    name.append(key)
                else:
                    locn=loc_counts.most_common(2)[1][1]
            if day >= 3 and locn/day >= 5/7:
                name.append(key)
df=df[~df['id'].isin(name)]
#去空值
df=df.dropna(axis=0)
useri=useri[useri['id'].isin(df['id'])]

