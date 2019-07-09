# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:10:02 2019

@author: 丁凡彧
"""

import pandas as pd
import numpy as np
import math
df = pd.read_csv('../../data/2/try(3-10)/use-poi-dropt1.csv')
user = df['id']
#排除重复用户和景点
user = list(set(user))
poi=df['poi']
poi=list(set(poi))
df2=pd.DataFrame(index=user)
pieces = dict(list(df.groupby('poi')))

for key in pieces:
    d=pieces[key]
    pieces2=dict(d['id'].value_counts())
    for key2 in pieces2:
        t=str(key)
        df2.loc[key2,t]=pieces2[key2]
df2=df2.fillna(0)
#df2.to_csv('../data/TJ/new-user-poi-afterTJ-34w(10-120).csv')
#矩阵分解
U,Sigma,V=np.linalg.svd(np.mat(df2),full_matrices=False)
Sig2=Sigma**2 #计算平方和
print(sum(Sig2))
print(sum(Sig2)*0.95) #取前90%
#sum(Sig2[:6]) #>90% SVD取前三个特征值
for i in range(len(Sig2)):
    if sum(Sig2[:i])>sum(Sig2)*0.95:
        n=i
        break
print(n)
U=U[:,0:n]
V=V[0:n,:]
Du=pd.DataFrame(U,index=df2.index.tolist())
Du = (Du - Du.min()) / (Du.max() - Du.min())#归一化
#Du = (Du - Du.mean()) / Du.std()#标准化
#Du = (Du -  np.mean(Du.mean())) / (np.max(Du.max()) - np.min(Du.min()))#均值归一化
Dv=pd.DataFrame(V,columns=df2.columns.values.tolist())
#Dv = (Dv - Dv.min(axis=1)) / (Dv.max(axis=1) - Dv.min(axis=1))
#Dv = (Dv - np.mean(Dv.mean())) / (np.max(Dv.max()) - np.min(Dv.min()))
#用户移动互联网使用情况特征向量
useri = pd.read_csv('../../data/alluser-i.csv')
#列命名
useri.columns=['id', 0,1,2,3,4,5,6,7,8,9]
#筛选交集
useri=useri[useri['id'].isin(Du.index.tolist())]
useri=useri.set_index('id')
#移动互联网使用情况向量归一化
useri = (useri - useri.mean()) / (useri.std())
#useri = (useri - useri.mean()) / (useri.max() - useri.min())
#合并特征向量
result = pd.concat([Du, useri], axis=1)
#保存
result.to_csv('../../data/2/try_con/user-TZ2-161w.csv')
Dv=Dv.T
Dv=(Dv-Dv.min())/(Dv.max()-Dv.min())
#Dv=(Dv-Dv.mean())/(Dv.std())
Dv=Dv.T
Dv.to_csv('../../data/2/try_con/poi-TZ-161w-90%.csv',index=False)