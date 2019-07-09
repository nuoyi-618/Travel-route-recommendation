# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:22:28 2019

@author: 丁凡彧
"""
import pandas as pd 
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score,recall_score, f1_score
df =pd.read_csv('../../../data/2/try_con/user-TZ2-161w.csv',index_col=0)
y_train= pd.read_csv('../../../data/2/try_con/Y-train.csv',index_col=0)
y_test=pd.read_csv('../../../data/2/try_con/Y-test.csv',index_col=0)

x_train=df[df.index.isin(y_train.index.tolist())]
x_test=df[df.index.isin(y_test.index.tolist())]
x_train=x_train.iloc[:,:10]
x_test=x_test.iloc[:,:10]

y_train =y_train.values.argmax(axis=1)
y_true=y_test.values.argmax(axis=1)
#贝叶斯计算概率
clf = GaussianNB()
clf.fit(x_train, y_train)
y_pred=clf.predict(x_test)
#评估
p = precision_score(y_true, y_pred, average="weighted")
r = recall_score(y_true, y_pred, average="weighted")  
f1 = f1_score(y_true, y_pred, average="weighted")  
acc=precision_score(y_true, y_pred, average="micro")
print(p,r,f1)