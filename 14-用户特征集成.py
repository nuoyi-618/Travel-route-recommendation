# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:57:20 2018

@author: 丁凡彧
"""

import pandas as pd  
import numpy as np
#读取矩阵分解得到的用户特征
df = pd.read_csv('../data/TZXL/user-TZ-85w(10-100)-90%.csv',index_col=0,header=None) 
#用户移动互联网使用情况特征向量
useri = pd.read_csv('../data/alluser-i.csv')
#列命名
useri.columns=['id', 0,1,2,3,4,5,6,7,8,9]
#筛选交集
useri=useri[useri['id'].isin(df.index.tolist())]
useri=useri.set_index('id')
#移动互联网使用情况向量归一化
useri = (useri - useri.mean()) / (useri.std())
#合并特征向量
result = pd.concat([df, useri], axis=1)
#保存
result.to_csv('../data/user-TZ/user-TZ2-85w(10-100)-90%.csv')