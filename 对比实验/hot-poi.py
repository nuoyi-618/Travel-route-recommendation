# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:00:58 2018

@author: 丁凡彧
"""

import pandas as pd  
import random
from collections import Counter
train_x = pd.read_csv('../../data/2/try_con/X-train.csv',index_col=0) 
test_x = pd.read_csv('../../data/2/try_con/X-test.csv',index_col=0) 
train_y= pd.read_csv('../../data/2/try_con/Y-train-db.csv',index_col=0)
test_y=pd.read_csv('../../data/2/try_con/Y-test-db.csv',index_col=0)
df = pd.read_csv('../../data/2/try(3-10)/use-poi-dropt1.csv') 

user=df.drop_duplicates(['id'])['id'].tolist()
#随机抽取30%的测试集用户 
test_user = test_x.index.tolist()
test_user = list(set(test_user))
train=df[~df['id'].isin(test_user)]
test=df[df['id'].isin(test_user)]
#统计访问人数最多的景点

hot_poi=Counter(train['poi']).most_common(5)
poi1=hot_poi[0][1]
#test_y=test_y['0'].value_counts()#测试用户实际访问景点数量

pieces = dict(list(test.groupby('id')))
y_pred=[]
num=0#预测准确的计数器
for key in pieces:
    d=pieces[key]
    d_pass=d['poi'].tolist()
    train_common=train[~train['poi'].isin(d_pass)]
    hot_poi=Counter(train_common['poi']).most_common(1)[0][0]
    y_pred.append(hot_poi)
    if hot_poi==test_y.loc[key,'0']:
        num=num+1


test_user_num=len(test_user)#测试总人数
acc=num/(test_user_num)
print(acc)
'''
#评估
for i in range(1):
    pre=hot_poi[i][0]
    num=num+test_y[pre]
    acc=num/(test_user_num*(i+1))
print(acc)
 '''
