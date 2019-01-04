# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:29:44 2018

@author: 丁凡彧
"""
import pandas as pd  
import sklearn.cluster as skc  # 密度聚类
from sklearn import metrics   # 评估模型
import matplotlib.pyplot as plt  # 可视化绘图
from sklearn.preprocessing import MinMaxScaler

train =pd.read_csv('../../data/more-poi/YCL-user-poi-246w(3).csv') 

useri = pd.read_csv('../../data/alluser-i.csv',index_col=0)
useri.columns=[0,1,2,3,4,5,6,7,8,9]
#获得用户训练矩阵
train=train.drop_duplicates(['id'])
train_name=list(train['id'])
train_user=useri[useri.index.isin(train_name)]

#标准化
train_user = (train_user - train_user.mean()) / (train_user.std())

X_train=train_user.values


db = skc.DBSCAN(eps=0.5, min_samples=10).fit(X_train) #DBSCAN聚类方法 还有参数，matric = ""距离计算方法
labels = db.labels_  #和X同一个维度，labels对应索引序号的值 为她所在簇的序号。若簇编号为-1，表示为噪声

print('每个样本的簇标号:')
print(labels)

raito = len(labels[labels[:] == -1]) / len(labels)  #计算噪声点个数占总数的比例
print('噪声比:', format(raito, '.2%'))

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  # 获取分簇的数目

print('分簇的数目: %d' % n_clusters_)
train['label']=labels
#print("轮廓系数: %0.3f" % metrics.silhouette_score(X_train, labels)) #轮廓系数评价聚类的好坏

