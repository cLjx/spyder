# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:15:39 2018

@author: administered
"""

import numpy as np, pandas as pd


# =============================================================================
# #python数据分析之pandas学习
# #https://www.cnblogs.com/nxld/p/6058591.html
# =============================================================================

# =============================================================================
# Series的创建
# =============================================================================

arr1 = np.arange(10)

print(arr1)

print(type(arr1))

print(isinstance(arr1,np.ndarray))

s1 = pd.Series(arr1)

print(s1)

print(type(s1))

dic1 = {'a':10,'b':20,'c':30,'d':40,'e':50}

print(dic1)

print(type(dic1))

s2 = pd.Series(dic1)

print(s2)

print(type(s2))

# =============================================================================
# #DataFrame的创建
# =============================================================================

arr2 = np.array(np.arange(12)).reshape(3,4)

print(arr2)

print(type(arr2))

df1 = pd.DataFrame(arr2)

print(df1)

print(type(df1))

dic3 = {'one':{'a':1,'b':2,'c':3,'d':4},
        'two':{'a':5,'b':6,'c':7,'d':8},
        'three':{'a':9,'b':10,'c':11,'d':12}}

print(dic3)

type(dic3)

df3 = pd.DataFrame(dic3)

print(df3)

print(type(df3))

df4 = df3[['one','three']]

print(df4)

s3 = df3['one']

print(s3)

# =============================================================================
# #数据索引index
# =============================================================================

s4 = pd.Series(np.array([1,1,2,3,5,8]))

print(s4)

print(s4.index)

s4.index = ['a','b','c','d','e','f']

print(s4)

print(s4[3])

print(s4['e'])

print(s4[[1,3,5]])

print(s4[1:3])

s5 = pd.Series(np.array([10,15,20,30,55,80]),\
               index = ['a','b','c','d','e','f'])

print(s5)

s6 = pd.Series(np.array([12,11,13,15,14,16]),\
               index = ['a','c','g','b','d','f'])

print(s6)

print(s5+s6)

print(s5/s6)

# =============================================================================
# #利用pandas查询数据
# =============================================================================
#C:\\Users\\administered\\Desktop\\testcsv.csv
mdata = pd.io.parsers.read_csv('test_csv.csv')

print(mdata.head())

print(mdata.tail())

print(mdata.loc[[2,3,4]])

print(mdata[['name','yw']])

print(mdata.loc[[2,3],['name','en']])

print(s5)

print(s5[['d','e']])

print(df3)

print(df3.loc['b','two'])

print(df3['two'])

print(df3.loc['b'])

print(df3.loc['b'].loc['two'])

print(df3.loc['b']['two'])

print(mdata)

print(mdata[mdata['yw']==1])

print(mdata['yw']==1)

print(mdata[1:2])
print(mdata.loc[1])

print(mdata[1:2]['yw'])
print(mdata.loc[1]['yw'])
print(mdata.loc[1:2]['yw'])

#print(mdata)
#print(mdata[1:2])
#print(mdata['yw'])
#print(mdata.loc[[1,2,3],['yw']])
#
##print(mdata[(mdata['yw'==1]) & (mdata['sx']>2)])
#
#print(mdata)
#
#print(mdata[mdata['sx']>2][['sx','name']])
#
#print(mdata[(mdata['yw']==1) & (mdata['sx']>2)])
#
## =============================================================================
## #统计分析
## =============================================================================
#
#np.random.seed(1234)
#
#d1 = pd.Series(2*np.random.normal(size = 100)+3)
#d2 = np.random.f(2,4,size = 100)
#d3 = np.random.randint(1,100,size = 100)
#
#print(d1)
#print(d2)
#print(d3)
#
#print(d1.count())
#
#print(d1.min())
#print(d1.max())
#
#print(d1.idxmin())
#print(d1.idxmax())
#
#print(d1.quantile(0.1))
#
#print(d1.sum())
#
#print(d1.mean())
#
##print(d1.mode())
#
#print(d1.var())
#
#print(d1.std())
#
#print(d1.describe())
#
#def stats(x):
#    return pd.Series([x.max(),x.min()],index=['max','min'])
#
#print(stats(d1))
#
#print(np.array([d1,d2,d3]).T)
#
#df = pd.DataFrame(np.array([d1,d2,d3]).T,columns=['x1','x2','x3'])
#
#print(df.head())
#
#print(df.apply(stats))
#
#print(df['x1'].describe())
#
#print(df.corr())
#
#print(df.corrwith(df['x1']))
#
#print(df.cov())
#
## =============================================================================
## #类似sql的操作
## =============================================================================
#
#dic = {'Name':['LiuSX','ZHANGS'],'Sex':['M','F'],'Age':[27,23],'Height':[165.7,167.2],\
#       'Weight':[61,63]}
#student2 = pd.DataFrame(dic)
#
#print(student2)
#
#tempdic = {'Name':['FANX','ZHOWS'],'Sex':['F','M'],'Age':[22,21],'Height':[168,171],\
#       'Weight':[51,69]}
#student = pd.DataFrame(tempdic)
#
#print(student)
#
#student3 = pd.concat([student,student2])
#
#print(student3)
#
#temp = pd.DataFrame(student2,columns=['Age','Height','Name','Sex','Weight','Score'])
#
#print(temp)
#
##del student2
##
##print(student2)
#print()
#print(student)
#print(student.drop([0]))
#print(student)
#
#print('\n')
#print(student3)
#print(student3[student3['Age']>22])
#print(student3)
#
#print(student3[student3['Age']>22].count()['Name'])
#
#print('\n')
#print(student3)
#print(student3.drop(['Age','Height'],axis=1))
#print(student3)
#
#student3.loc[student3['Name']=='FANX','Weight'] = 55
#
#print(student3)
#
#print(student3.groupby('Sex').mean())
#
#print(student3.drop('Age',axis=1).groupby('Sex').mean())
#
#series = pd.Series(np.array(np.random.randint(1,20,10)))
#print(series)
#print(np.array([series,series.sort_values()]).T)
#print(series.sort_values(ascending=False))
#
#print(series)
#
#print('\n')
#print(student3)
#
#score = pd.DataFrame({'Name':['FANX','LiuSX'],'Score':[99,98]})
#print(score)
#stu_score1 = pd.merge(student3,score,on='Name')
#print(stu_score1)
#
#print('\n')
#print(student3)
#
#stu_score2 = pd.merge(student3,score,on='Name', how = 'left')
#
#print(stu_score2)
#
#s = stu_score2['Score']
#
#print(s)
#
#print(sum(pd.isnull(s)))
#
#print(s.dropna())
#
#print(s)
#
## =============================================================================
## #数据透视表
## =============================================================================
#
#print('\n')
#
#print(student3)
#
#print(pd.pivot_table(student3,values=['Age'],columns=['Sex']))
#
#print(pd.pivot_table(student3,values=['Age','Height'],columns=['Sex']))
#
#print(student3.groupby('Sex').mean())
#
#
## =============================================================================
## #多层索引的使用
## =============================================================================
#print('\n')
#
#
#print(student3)
#
#print(student3['Sex'])
#
#print(student3.loc[[0],['Sex','Age']])
#
#print(len(student3))
#
#
##test
#
#print('\n')
#
#a = (('a','b','c'),(1,2,3),(4,5,6),(7,8,9))
#
#print(a)
#
#print(type(a))
#
#df = pd.DataFrame(np.array(a))
#
#print(df)
#
##list_= print(list(a))
##
##print(type(list_))
##
##df_ = pd.DataFrame(np.array(a))
##
###print(a[1])
#
#print(df.loc[[0]])
#
#new = df.loc[[0]].to_dict('list')
#print(new)
#print(type(new))
#print(new[1][0])
#
##test time
#import time
#
#df = pd.DataFrame(np.array([1509802521,1509802531,1509802539,1509802540]),columns=['time'])
#
#print(df)
#
#def fun_df_time(x):
#    temp = time.localtime(x)
#    Y = time.strftime('%Y',temp)
#    m = time.strftime('%m',temp)
#    d = time.strftime('%d',temp) 
#    H = time.strftime('%H',temp)
#    M = time.strftime('%M',temp) 
#    S = time.strftime('%S',temp)
##    return {'Y':Y,'m':m,'d':d,'H':H,'M':M,'S':S}
##    return pd.DataFrame({'Y':Y,'m':m,'d':d,'H':H,'M':M,'S':S})
##    return pd.DataFrame({'Y':[Y],'m':[m],'d':[d],'H':[H],'M':[M],'S':[S]})
#    return S
#
#
##df['Y'] = None
##df['m'] = None
##df['d'] = None
##df['H'] = None
##df['M'] = None
##df['S'] = None
##
##for index,row in df.iterrows():
##    print(index)
##    df.loc[[index],['Y','m','d','H','M','S']] = fun_df_time(row['time'])
#
#df['Y'] = df.apply(lambda row:fun_df_time(row['time']),axis = 1)
#
#
#
#print(df)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
