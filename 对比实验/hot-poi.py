# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:00:58 2018

@author: 丁凡彧
"""

import pandas as pd  
import random
from collections import Counter

df = pd.read_csv('../../data/2/161w/user-poi.csv') 

user5id =pd.read_csv('../../data/more-poi/YCL-user-poi-246w(3).csv') 
name=user5id.drop_duplicates(['id'])
name=list(name['id'])
df=df[df['id'].isin(name)]

df=df.drop_duplicates(['id','poi'])
user=df.drop_duplicates(['id'])['id'].tolist()
#随机抽取20%的测试集用户 
test_user = random.sample(user, int(len(user)*0.3))
train=df[~df['id'].isin(test_user)]
test=df[df['id'].isin(test_user)]
#统计访问人数最多的景点

hot_poi=Counter(train['poi']).most_common(5)
poi1=hot_poi[0][1]
test_y=test['poi'].value_counts()#测试用户实际访问景点数量

test_user_num=len(test_user)#测试总人数
num=0#预测准确的计数器
#评估
for i in range(3):
    pre=hot_poi[i][0]
    num=num+test_y[pre]
    acc=num/(test_user_num*(i+1))
print(acc)
train.to_csv('../../data/more-poi/test/tarin(3).csv',index=False)
test.to_csv('../../data/more-poi/test/test(3).csv',index=False)   