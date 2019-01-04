# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:48:51 2018

@author: 丁凡彧
"""

import pandas as pd  
import numpy as np
#读取输入集X
X = pd.read_csv('../data/2/new-X-161w(6-100)-1.csv',index_col=0)
pieces = dict(list(X.groupby(X.index)))
Nx=[]
#初始化添加0向量长度
ling=[0]*X.shape[1]
del X
#不足最长访问序列的用户进行补零
for key in pieces:
    d=pieces[key].reset_index(drop=True)
    for i in range(len(d)):
        l=d.loc[i].tolist()
        Nx.append(l)
    for j in range(13-len(d)):
        Nx.append(ling)
N1 = pd.DataFrame(Nx[:int(len(Nx)/2)])        
N2 = pd.DataFrame(Nx[int(len(Nx)/2):])
del Nx
del pieces
frames=[N1,N2]
df=pd.concat(frames)
df.to_csv('../data/2/new-X-161w(6-100)-1.csv',index=False)
