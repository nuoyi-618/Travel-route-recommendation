# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:11:16 2019

@author: 丁凡彧
"""

import numpy as np
import pandas as pd
from keras_layer_normalization import LayerNormalization  
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score,recall_score, f1_score
from keras.models import load_model
test_x = pd.read_csv('../../data/2/try_con/TX-test-svd.csv')
y_true=pd.read_csv('../../data/2/try_con/Y-test-svd.csv',index_col=0)
#test_x = pd.read_csv('../../data/2/try_cnn/TX-test.csv',index_col=0) 
y_true=y_true.values.argmax(axis=1)

'''
x=[]
for i in range(19,28):
    x.append(i)
x.append(49)
x.append(48)
x.append(47)
test_x.drop(test_x.columns[x], axis=1, inplace=True)
'''
test_x=test_x.values
test_x = test_x.reshape((y_true.shape[0],9, test_x.shape[1]))
sw = compute_sample_weight(class_weight='balanced',y=y_true)
model = load_model('result/BiGRU_1_50_noLN_svd.h5' ,custom_objects={"LayerNormalization":LayerNormalization})
#model = load_model('result/CNN_1_50.h5')      
y_pred = model.predict(test_x,batch_size=1,verbose=0)
y_pred = y_pred.argmax(axis=1)
cm =confusion_matrix(y_true, y_pred, sample_weight=sw)
#计算P、R、F1值
p = precision_score(y_true, y_pred, average="weighted")
r = recall_score(y_true, y_pred, average="weighted") 
f1 = f1_score(y_true, y_pred, average="weighted")  
print(p,r,f1)