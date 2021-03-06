# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:02:01 2018

@author: 丁凡彧
"""

import pandas as pd  
from keras.models import Sequential
from keras.layers import Dense, Dropout,Bidirectional
from keras.layers import Masking,BatchNormalization
from keras.layers import GRU
from keras import initializers,optimizers
from keras_layer_normalization import LayerNormalization
from matplotlib import pyplot
#X训练集               
train_x = pd.read_csv('../../data/2/try_con/TX-train-svd.csv') 
test_x = pd.read_csv('../../data/2/try_con/TX-test-svd.csv') 

#读取Y集合即标签集
train_y= pd.read_csv('../../data/2/try_con/Y-train-svd.csv',index_col=0)
test_y=pd.read_csv('../../data/2/try_con/Y-test-svd.csv',index_col=0)

train_x=train_x.fillna(0)
#转化为矩阵
x_train=train_x.values
y_train = train_y.values
x_val=test_x.values
y_val = test_y.values

#转换训练集为3D集合[样本，时间步，特征]
x_train = x_train.reshape((y_train.shape[0],9, x_train.shape[1]))
x_val = x_val.reshape((y_val.shape[0],9, x_val.shape[1]))
print(x_train.shape, y_train.shape,x_val.shape, y_val.shape)

#序列搭建模型
model = Sequential()
#屏蔽层，屏蔽0输入内容
model.add(Masking(mask_value=0,input_shape=(9,50)))
#双向GRU模型
#model.add(Dropout(0.5))
model.add(LayerNormalization())
model.add(Bidirectional(GRU(31,input_shape=(x_train.shape[1], x_train.shape[2]))))
model.add(Dropout(0.5))
#对应31个景点one-hot向量的输出层
#model.add(Dense(31, activation='relu'))
model.add(Dense(31, activation='softmax'))
#采用adam优化器
rmsprop = optimizers.RMSprop(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics = ['accuracy'])
# 训练网络
history = model.fit(x_train, y_train, epochs=50, batch_size=128, 
                    verbose=2, validation_data=(x_val, y_val))
# 打印训练曲线
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()
pyplot.plot(history.history['acc'], label='train')
pyplot.plot(history.history['val_acc'], label='test')
pyplot.legend()
pyplot.show()
#保存模型
model.save('result/BiGRU_1_50-svd.h5')
result=[history.history['loss'],history.history['val_loss'],history.history['acc'],history.history['val_acc']] 
result=pd.DataFrame(result)
result=result.T
result.columns=['loss','Val_loss','acc','val_acc']
result.to_csv('result/BiGRU_1_50-svd.csv',index=False)