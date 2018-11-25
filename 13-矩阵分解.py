# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 17:45:10 2018

@author: 丁凡彧
"""

import pandas as pd  
import numpy as np


df = pd.read_csv('../data/TJ/new-user-poi-afterTJ-246w(10-100).csv',index_col=0) 
U,Sigma,V=np.linalg.svd(np.mat(df),full_matrices=False)
Sig2=Sigma**2 #计算平方和
print(sum(Sig2))
print(sum(Sig2)*0.9) #取前90%
#sum(Sig2[:6]) #>90% SVD取前三个特征值
for i in range(len(Sig2)):
    if sum(Sig2[:i])>sum(Sig2)*0.9:
        n=i
        break
print(n)
'''
U=U[:,0:n]
V=V[0:n,:]
Du=pd.DataFrame(U,index=df.index.tolist())
Du = (Du - Du.min()) / (Du.max() - Du.min())
Du.to_csv('../data/TZXL/user-TZ-85w(10-100).csv',header=None)
Dv=pd.DataFrame(V,columns=df.columns.values.tolist())
Dv = (Dv - Dv.min()) / (Dv.max() - Dv.min())
Dv.to_csv('../data/TZXL/poi-TZ-85w(10-100).csv',index=False)
'''