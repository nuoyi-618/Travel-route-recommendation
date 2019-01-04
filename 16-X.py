# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:53:02 2018

@author: 丁凡彧
"""
import pandas as pd  
import numpy as np
import time
st = time.time()
df = pd.read_csv('../data/2/poi-TZ(KeDaXing)-161w(6-100).csv')#可达性
poi = pd.read_csv('../data/2/new-poi-TZ3-161w(6-100).csv')#景点特性
user=pd.read_csv('../data/2/user-TZ2-161w(6-100).csv',index_col=0)#用户特征
user.columns=list(range(24))

X=[]#特征向量
Xkey=[]#用户编号
#按用户id分组，逐一处理
a=list(df.groupby('id'))
#数据过大，分割处理数据集
pieces = dict(a[int(len(a)/2):])
#pieces = dict(a)
for key in pieces:    
    d=pieces[key].reset_index(drop=True)
    pieces[key]=1
    d.sort_values(by=['date','time'])
    for i in range(d.shape[0]-1):
        Xkey.append(key)
        #取用户当前访问景点特征向量
        poinum=d.loc[i,'poi']
        idnum=d.loc[i,'id']
        poitz=poi[str(poinum)].tolist()
        #添加可达性至用户特征向量
        poitz.append(d.loc[i,'kdx'])
        #用户特征向量与景点特征向量相乘得到用户特征矩阵
        usertz=list(user.loc[idnum])
        poitz=np.mat(poitz)
        usertz=np.mat(usertz)
        tzjz=np.array(poitz.T*usertz)
        #展开矩阵得到当前用户访问当前景点的特征向量，为时间序列中的一节
        c=tzjz.flatten()
        c=c.tolist()
        X.append(c)
N=pd.DataFrame(X)
N=N.set_index([Xkey])
N.to_csv('../data/2/new-X-161w(6-100)-2.csv')
#计算耗时
st1 = time.time()
time=(st1-st)/60
print('time:',time)
