# -*- coding: utf-8 -*-
"""
Created on Fri May 24 21:30:45 2019

@author: 丁凡彧
"""
import pandas as pd  
import numpy as np
import time
import random
st = time.time()
df = pd.read_csv('../../data/2/try(3-10)/poi-TZ(KeDaXing)-161w.csv')#可达性
poi = pd.read_csv('../../data/2/try_con/poi-TZ3-161w.csv')#景点特性
user=pd.read_csv('../../data/2/try_con/user-TZ2-161w.csv',index_col=0)#用户特征
user.columns=list(range(23))
X=[]#特征向量
Xkey=[]#用户编号
Y=[]
Ykey=[]
#按用户id分组，逐一处理
a=list(df.groupby('id'))
#数据过大，分割处理数据集
pieces = dict(a)
#pieces = dict(a)
for key in pieces:    
    d=pieces[key].reset_index(drop=True)
    pieces[key]=1
    d=d.sort_values(by=['date','time'])
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
        c=usertz+poitz
        X.append(c)
    for i in range(d.shape[0]):
        poinum=d.loc[i,'poi']
        idnum=d.loc[i,'id']
        #用户访问的最后一个景点即为Ykey
        if i==d.shape[0]-1:
            Y.append(poinum)
            Ykey.append(key)

Nx=pd.DataFrame(X)
Nx=Nx.set_index([Xkey])
'''
test_user = random.sample(list(Nx.index), int(len(user)*0.3))
'''
test_user = pd.read_csv('../../data/2/try_con/X-test.csv',index_col=0) 
test_user=test_user.index.tolist()
train_x=Nx[~Nx.index.isin(test_user)]
test_x=Nx[Nx.index.isin(test_user)]

train_x.to_csv('../../data/2/try_con/X-train.csv')
test_x.to_csv('../../data/2/try_con/X-test.csv')
#对景点矩阵进行one-hot编码
onehot= pd.get_dummies(Y)
Ny=pd.DataFrame(onehot)
Ny=Ny.set_index([Ykey])
train_y=Ny[~Ny.index.isin(test_user)]
test_y=Ny[Ny.index.isin(test_user)]
train_y.to_csv('../../data/2/try_con/Y-train-db.csv')
test_y.to_csv('../../data/2/try_con/Y-test-db.csv')

#计算耗时
st1 = time.time()
time=(st1-st)/60
print('time:',time)
