# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:16:13 2018

@author: 丁凡彧
"""

import pandas as pd  
from collections import Counter

all_user_poi = pd.read_csv('../../data/2/161w/user-poi.csv')
df = pd.read_csv('../../data/more-poi/test/dbscan(5).csv') 
test_user_poi =pd.read_csv('../../data/more-poi/test/test(5).csv') 
name=test_user_poi.drop_duplicates(['id'])
name=list(name['id'])
train_user=df[~df['id'].isin(name)]
test_user=df[df['id'].isin(name)]

def pre(train,test):
    num=0
    hot_poi=Counter(train['poi']).most_common(5)
    test_y=test['poi'].value_counts()#测试用户实际访问景点数量
    for i in range(2):
        pre=hot_poi[i][0]
        if pre in test['poi']: 
            num=num+test_y[pre]
    return num

pieces = dict(list(test_user.groupby('label')))
sum_pre=0

for key in pieces:
    if key!=-1:        
        d=pieces[key].reset_index(drop=True)
        test_name=d.drop_duplicates(['id'])
        test_name=list(test_name['id'])
        test=test_user_poi[test_user_poi['id'].isin(test_name)]
        train_name=list(train_user[(train_user.label==key)]['id'])
        train=all_user_poi[all_user_poi['id'].isin(train_name)]
        sum_pre=sum_pre+pre(train,test)

print(sum_pre/(len(name)*3))    
    




