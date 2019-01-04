# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 10:42:11 2018

@author: 丁凡彧
"""
import pandas as pd
import haversine as ha
df = pd.read_csv('../data/FG/FG-user-poi-85w(10-100).csv')
poi = pd.read_csv('../data/poi-38-wgs84.csv') #读取poi
poi.columns=['id','lng','lat','name','type']
#按用户编号分类
pieces = dict(list(df.groupby('num')))
kdx=[]
poi.set_index(['id'],inplace = True)
#循环计算各个用户上一景点与下一个景点间可达性
#可达性梯度编号，1——dis<=500;2——500<dis<=1000;3——1000<dis<=2000;4——2000<dis<=5000;5>5000
for key in pieces:
    d=pieces[key].reset_index(drop=True)
    d.sort_values(by=['date','time'])
    for i in range(d.shape[0]):
        poinum=d.loc[i,'poi']
        if i==0:
            dis=ha.haversine(d.loc[i,'lng'],d.loc[i,'lat'],poi.loc[poinum,'lng'],poi.loc[poinum,'lat'])
        else:
            dis=ha.haversine(d.loc[i-1,'lng'],d.loc[i-1,'lat'],poi.loc[poinum,'lng'],poi.loc[poinum,'lat'])
        dis=abs(dis)
        if dis<=500:
            dtype=1
        elif 500<dis and dis<=1000:
            dtype=2
        elif 1000<dis and dis<=2000:
            dtype=3
        elif 2000<dis and dis<=5000:
            dtype=4
        elif 5000<dis:
            dtype=5
        kdx.append(dtype)
df=df.sort_values(by=['num','date','time'])
df['kdx']=kdx
df.to_csv('../data/poi-TZ/poi-TZ(KeDaXing)-85w(10-100)-90%.csv',index=False)
        
            
        
