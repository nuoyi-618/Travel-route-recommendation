# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:16:43 2018

@author: 丁凡彧
"""

import pandas as pd  
import numpy as np
#读取矩阵分解得到的景点特征向量
df = pd.read_csv('../data/2/new-poi-TZ2-161w(6-100).csv') 
#读取景点poi文件
poi_i = pd.read_csv('../data/poi-38-wgs84.csv') 
#景点取交集
int_list=list(df.columns)
int_list=[int(float(x)) for x in int_list]
poi_i=poi_i[poi_i['id'].isin(int_list)]
#景点按编号分类
poi_i.sort_values(by=['id'])
#添加景点类型至景点特征向量
poi_type=poi_i['type'].tolist()
poitype = pd.DataFrame(poi_type).T
poitype.columns = df.columns
df = pd.concat([df,poitype])
df.to_csv('../data/2/new-poi-TZ3-161w(6-100).csv',index=False)