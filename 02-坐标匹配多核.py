"""
Created on Tue Jul  3 11:44:39 2018

@author: 丁凡彧
"""
import multiprocessing as mp
from multiprocessing import freeze_support
import pandas as pd  
import haversine as ha
import time

df = pd.read_csv('../data/userloc-wgs84/userloc0.csv', header=None)
df.columns=['date','time','id','lng','lat']
poi = pd.read_csv('../data/new-poi-wgs84.csv', header=None) #读取poi
poi.columns=['name','lng','lat','type']

df['poi']=None
def job(j):
    dis=500
    c=None
    for i in range(0,poi.shape[0]):
        dis1=ha.haversine(poi.loc[i,'lng'],poi.loc[i,'lat'],df.loc[j,'lng'],df.loc[j,'lat'])
        if  dis1<dis:
            dis=dis1
            c=i
    return c

def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(1000000))
    return res

if __name__ == '__main__':
    freeze_support()
    st = time.time()
    ru=multicore()
    st1 = time.time()
    time=(st1-st)/60
    print('multithread time:',time)
