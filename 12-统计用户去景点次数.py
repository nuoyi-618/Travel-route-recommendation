# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 08:55:19 2018

@author: 丁凡彧
"""

import pandas as pd
import math
df = pd.read_csv('../data/YCL-user-poi-246w.csv')
user = df['id']
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
