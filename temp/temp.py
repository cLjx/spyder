# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import sys

ticks = time.time()

t = time.localtime()



print(ticks)

print(t)


print(time.mktime(t))

print(time.localtime(ticks))

x = time.localtime(ticks)

print()

print(x)
print(type(x))

print(time.strftime('%Y',x))

#print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1418992496)))
#
#if isinstance("dsf",str):
#    print(type("dsf"))
#else:
#    print("dsf")
#    
##sys.exit()
#    
#if isinstance(23,str):
#    print(type(223))
#else:
#    print(24)
#print(65465413215132156)
#
#print(time.strptime('2014-12-19 20:34:56','%Y-%m-%d %H:%M:%S'))
#
#aaa=((1,2,3),(1,2))
#print(len(aaa))

#SELECT MIN(create_time) as min, MAX(create_time) as max  FROM ods_wei_order_info as minfo WHERE create_time > 0 
print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(1417708257)))
print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(1525343799)))

print(time.mktime(time.strptime('2017-11-4 20-00-00','%Y-%m-%d %H-%M-%S')))

print(time.mktime(time.strptime('2017-11-5 6-00-00','%Y-%m-%d %H-%M-%S')))

#import pandas as pd
#import os
#
##df_temp = pd.read_csv('csv_temp/mStTiPro.csv')
##
##df_temp.header()
#if not os.path.exists('csv_temp'):
#    os.makedirs('csv_temp')
#
#if os.path.exists('csv_temp/mStTiPro_df.csv'):
#    os.remove('csv_temp/mStTiPro_df.csv')
#file = open('csv_temp/mStTiPro_df.csv','w')
#file.close()
#if os.path.exists('csv_temp/mStTiPro_info.csv'):
#    os.remove('csv_temp/mStTiPro_info.csv')
#file = open('csv_temp/mStTiPro_info.csv','w')
#file.close()
#
#file = open('csv_temp/mStTiPro_df_ mst.stid = 10387 _2015-06-20 2018-09-18.csv','w')
#file.close()



print(time.strftime('%Y/%m/%d',time.localtime(1525343799)))

import numpy as np
n =  np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)

n=pd.DataFrame(n)
n.columns=['a','b','c']
print(n['b'][0])


print(time.mktime(time.strptime('2015-9-22 00-00-00','%Y-%m-%d %H-%M-%S')))

print(time.mktime(time.strptime('2015-9-23 0-00-00','%Y-%m-%d %H-%M-%S')))


