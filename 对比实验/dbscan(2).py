# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:16:13 2018

@author: 丁凡彧
"""

import pandas as pd  
from collections import Counter

all_user_poi = pd.read_csv('../../data/2/try(3-10)/use-poi.csv')
df = pd.read_csv('../../data/2/try(3-10)/dbscan3.csv') 
test_user_poi =pd.read_csv('../../data/2/try_con/X-test.csv',index_col=0) 
test_y=pd.read_csv('../../data/2/try_con/Y-test-db.csv',index_col=0)

all_user_poi=all_user_poi[all_user_poi['id'].isin(df['id'].tolist())]
test_user_poi=test_user_poi[test_user_poi.index.isin(df['id'].tolist())]
test_y=test_y[test_y.index.isin(df['id'].tolist())]

name=test_user_poi.index.tolist()
name = list(set(name))

train_user=df[~df['id'].isin(name)]
test_user=df[df['id'].isin(name)]

df_name=df['id'].tolist()


y_pred=[]
#计算当前分类用户除测试用户已经去过的景点访问量最高的景点推荐
def pre(train,test):
    num=0
    hot_poi=Counter(train['poi']).most_common(1)
    pieces_test = dict(list(test.groupby('id')))
    for key_test in pieces_test:
        d=pieces_test[key_test]
        d_pass=d['poi'].tolist()
        train_common=train[~train['poi'].isin(d_pass)]
        hot_poi=Counter(train_common['poi']).most_common(1)[0][0]
        y_pred.append(hot_poi)
        if hot_poi==test_y.loc[key_test,'0']:
            num=num+1
    return num

pieces = dict(list(test_user.groupby('label')))
sum_pre=0

for key in pieces:
#    if key!=-1:        
    d=pieces[key].reset_index(drop=True)
    test_name=d.drop_duplicates(['id'])
    test_name=list(test_name['id'])
    test=df[df['id'].isin(test_name)]
    train_name=list(train_user[(train_user.label==key)]['id'])
    train=all_user_poi[all_user_poi['id'].isin(train_name)]
    sum_pre=sum_pre+pre(train,test)

print(sum_pre/(len(name)))    

from sklearn.metrics import precision_score,recall_score, f1_score

p = precision_score(test_y['0'], y_pred, average="weighted") 
r = recall_score(test_y['0'], y_pred, average="weighted") 
f1 = f1_score(test_y['0'], y_pred, average="weighted")  
print(p,r,f1)
