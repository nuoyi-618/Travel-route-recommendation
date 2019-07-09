# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:26:21 2019

@author: 丁凡彧
"""

import pandas as pd
import matplotlib.pyplot as plt
'''
df = pd.read_csv('../../code/try/result/BiGRU_1_50.csv') 
plt.plot(df['loss'] ,'--',label='train',linewidth=2)
plt.plot(df['val_loss'],label='test',linewidth=2)
plt.grid(alpha=0.4)
plt.xlabel('epoch')
plt.legend()
plt.savefig('BiGRU_loss.png')
plt.show()   
plt.plot(df['acc'],'--' ,label='train',linewidth=2)
plt.plot(df['val_acc'],label='test',linewidth=2)
plt.grid(alpha=0.4)
plt.xlabel('epoch')
plt.legend()
plt.savefig('BiGRU_acc.png')
plt.show() 
'''
df2 = pd.read_csv('db_loss.csv',index_col=0) 
plt.plot(df2['Bi-GRU'] ,label='Bi-GRU',linewidth=2)
plt.plot(df2['RNN'],'--',label='RNN',linewidth=2)
plt.plot(df2['LSTM'],'-.' ,label='LSTM',linewidth=2)
plt.plot(df2['GRU'],':',label='GRU',linewidth=3)
plt.grid(alpha=0.4)
plt.xlabel('epoch')
#注释（x,y,内容\n换行，bbox边框）
#plt.text(35,0.3,'Bi-GRU:0.5163 \nRNN:0.4311 \nLSTM:0.4916 \nGRU:0.4924',bbox=dict(boxstyle='round,pad=0.5',fc='yellow',ec='k',lw=1,alpha=0.3))
#bbox_to_anchor表示legend的位置，前一个表示左右，后一个表示上下，framealpha边框透明度
plt.legend(loc='upper center',bbox_to_anchor=(0.5, 1.16),ncol=4,framealpha=0)
plt.savefig('db.png')
plt.show()

