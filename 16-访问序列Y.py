# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:56:31 2018

@author: 丁凡彧
"""
import pandas as pd  
import numpy as np
df = pd.read_csv('../data/poi-TZ/poi-TZ(KeDaXing)-85w(10-100)-90%.csv')
poi = pd.read_csv('../data/poi-TZ/poi-TZ3-85w(10-100)-90%.csv')
user=pd.read_csv('../data/user-TZ/user-TZ2-85w(10-100)-90%.csv',index_col=0)

Ykey=[]
pieces = dict(list(df.groupby('num')))
for key in pieces:
    d=pieces[key].reset_index(drop=True)
    d.sort_values(by=['date','time'])
    for i in range(d.shape[0]):
        poinum=d.loc[i,'poi']
        idnum=d.loc[i,'id']
        #用户访问的最后一个景点即为Ykey
        if i==d.shape[0]-1:
            Ykey.append(poinum)
#对景点矩阵进行one-hot编码
onehot= pd.get_dummies(Ykey)
onehot.to_csv('../data/Training/TY-85w(10-100)-90%.csv',index=False)
