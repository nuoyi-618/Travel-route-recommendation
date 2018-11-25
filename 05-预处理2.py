# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:22:24 2018

@author: 丁凡彧
"""

import pandas as pd
import math
df = pd.read_csv('../data/YCL-user-poi-246w.csv')

pieces = dict(list(df.groupby('id')))

name=[]

for key in pieces:
    d=pieces[key].reset_index(drop=True)
    d=d.drop_duplicates(['poi'])
    if d.shape[0] >=3:
        name.append(key)
'''
    if d.drop_duplicates(['date']).shape[0] > 2:
        d=d[(d["time"]> 7 ) & (d["time"] < 20) ]
        d=d.drop_duplicates(['date','poi'])
        if d.shape[0] > 2:        
            npoi=max(d['poi'].value_counts())
            nid=d.drop_duplicates(['date']).shape[0]
            if npoi/nid >= (4/7):
                name.append(key)
'''
df=df[df['id'].isin(name)]
