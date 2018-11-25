# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:48:43 2018

@author: 丁凡彧
"""

import pandas as pd  
#import haversine as ha
df = pd.read_csv('../data/2.csv')
poi = pd.read_csv('../data/use-poi-127.csv') #读取poi
'''
df['poi']=None
df['name']=None
for i in range(df.shape[0]):
    min=1000
    minid=None
    for j in range(poi.shape[0]):
        dis=ha.haversine(poi.loc[j,'x'],poi.loc[j,'y'],df.loc[i,'x'],df.loc[i,'y'])
        if dis<min:
            min=dis
            minid=poi.loc[j,'id']
            name=poi.loc[j,'name']
    df.loc[i,'name']=name
    df.loc[i,'poi']=minid
'''       
df['poi']=None
df['loc']=None
poi=poi.sort_values(by=['x','y'])
df=df.sort_values(by=['经度','纬度'])
a=list(df.groupby(['经度', '纬度']).size())

l=[]
lo=[]
for j in range(poi.shape[0]):
    p=poi.loc[j,'poi']
    loc=poi.loc[j,'id']
    for i in range(a[j]):
        l.append(p)
        lo.append(loc)
df['poi']=l       
df['loc']=lo       
    
'''
for i in range(df.shape[0]):
    for j in range(poi.shape[0]):
        if df.loc[i,'经度']==poi.loc[j,'x'] and df.loc[i,'纬度']==poi.loc[j,'x']:
            df.loc[i,'poi']=poi.loc[j,'poi']
'''
        