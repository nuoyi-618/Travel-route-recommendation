# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:31:21 2019

@author: 丁凡彧
"""
import pandas as pd
import math
import numpy as np
df = pd.read_csv('../../data/2/try(3-10)/use-poi-dropt1.csv') 
#print(df['poi'].value_counts())#统计频数
#df=df.dropna(axis=0)#去空值
pieces = dict(list(df.groupby('poi')))

poildx=[]
#高斯加权计算流行度
def gaussian(dist):
     c=30
     return math.e ** (-(dist) ** 2 / (2 * c ** 2))
for key in pieces:
    LXD=0
    d=pieces[key].reset_index(drop=True)
    for i in range(d.shape[0]):
        if(d.loc[i,'date']>20170430):
            dist=d.loc[i,'date']-20170500
        else:
            dist=20170430-d.loc[i,'date']
        LXD=LXD+gaussian(dist)
    poildx.append(LXD)
df2 = pd.read_csv('../../data/2/try_con/poi-TZ-161w-90%.csv') 
#标准化
def Z_ScoreNormalization(x,mu,sigma):
	x = (x - mu) / sigma;
	return x;
mu=np.mean(poildx)
sigma=np.std(poildx)
poildx2=[]
for i in poildx:
    poildx2.append(Z_ScoreNormalization(i,mu,sigma))
#添加特征向量
b = pd.DataFrame(poildx2).T
b.columns = df2.columns
df2 = pd.concat([df2,b])

#读取景点poi文件
poi_i = pd.read_csv('../../data/poi-38-wgs84.csv') 
#景点取交集
int_list=list(df2.columns)
int_list=[int(float(x)) for x in int_list]
poi_i=poi_i[poi_i['id'].isin(int_list)]
#景点按编号分类
poi_i.sort_values(by=['id'])
#添加景点类型至景点特征向量
poi_type=poi_i['type'].tolist()
poitype = pd.DataFrame(poi_type).T
poitype.columns = df2.columns
df3 = pd.concat([df2,poitype])
df3.to_csv('../../data/2/try_con/poi-TZ3-161w.csv',index=False)
