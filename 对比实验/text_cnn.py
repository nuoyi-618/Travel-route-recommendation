# -*- coding: utf-8 -*-
"""
Created on Wed May 22 23:19:32 2019

@author: 丁凡彧
"""
import pandas as pd  
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv1D, MaxPooling1D, Dropout, Input, concatenate
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from keras.models import Model
from matplotlib import pyplot
import os
import numpy as np


def text_cnn(maxlen=9, max_features=41, embed_size=31):
    # Inputs
    comment_seq = Input(shape=[maxlen], name='x_seq')

    # Embeddings layers
    emb_comment = Embedding(max_features, embed_size)(comment_seq)

    # conv layers
    convs = []
    filter_sizes = [2, 3, 4, 5]
    for fsz in filter_sizes:
        l_conv = Conv1D(filters=30, kernel_size=fsz, activation='relu')(emb_comment)
        l_pool = MaxPooling1D(maxlen - fsz + 1)(l_conv)
        l_pool = Flatten()(l_pool)
        convs.append(l_pool)
    merge = concatenate(convs, axis=1)

    out = Dropout(0.5)(merge)
    output = Dense(32, activation='relu')(out)

    output = Dense(units=31, activation='sigmoid')(output)

    model = Model([comment_seq], output)
    #     adam = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics = ['accuracy'])
    return model

if __name__ == '__main__':
    x_train = pd.read_csv('../../data/2/try_cnn/TX-train.csv',index_col=0) 
    x_test = pd.read_csv('../../data/2/try_cnn/TX-test.csv',index_col=0) 
    y_train= pd.read_csv('../../data/2/try_con/Y-train.csv',index_col=0)
    y_test=pd.read_csv('../../data/2/try_con/Y-test.csv',index_col=0)
    model = text_cnn()
    batch_size = 128
    epochs = 20
    history = model.fit(x_train, y_train, epochs=50, batch_size=128, 
                    verbose=2, validation_data=(x_test, y_test))
    scores = model.evaluate(x_test, y_test)
    print('test_loss: %f, accuracy: %f' % (scores[0], scores[1]))
    pyplot.plot(history.history['loss'], label='train')
    pyplot.plot(history.history['val_loss'], label='test')
    pyplot.legend()
    pyplot.show()
    pyplot.plot(history.history['acc'], label='train')
    pyplot.plot(history.history['val_acc'], label='test')
    pyplot.legend()
    pyplot.show()  