# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:44:52 2018

@author: administered
"""



import numpy as np
import csv

file_path=r'C:\Users\administered\Desktop\t.sql'
path=r'file_sql.sql'

import chardet
import os

def strJudgeCode(str):
    return chardet.detect(str)

def readFile(path):
    try:
        f = open(path, 'r')
        filecontent = f.read()
    finally:
        if f:
            f.close()

    return filecontent

def WriteFile(str, path):
    try:
        f = open(path, 'w')
        f.write(str)
    finally:
        if f:
            f.close()

def converCode(path):
    file_con = readFile(path)
    result = strJudgeCode(file_con)
    #print(file_con)
    if result['encoding'] == 'utf-8':
        #os.remove(path)
        a_unicode = file_con.decode('utf-8')
        gb2312 = a_unicode.encode('gbk')    
        WriteFile(gb2312, path)

def listDirFile(dir):
    list = os.listdir(dir)
    for line in list:
        filepath = os.path.join(dir, line)
        if os.path.isdir(filepath):
            listDirFile(filepath)
        else:
            print(line)
            converCode(filepath)            

if __name__ == '__main__':
    listDirFile(u'.\TRMD')















# =============================================================================
# #file_path=r'C:\Users\administered\Desktop\t.sql'
# #path=r'file_sql.sql'
# #data = []
# ## #读取
# #with open(file_path,encoding='utf-8',) as txtfile:
# #    line=txtfile.readlines()
# #    for i,rows in enumerate(line):
# ##        if i in range(5158,len(line)) :  #指定数据哪几行
# ##        print(rows)
# #        data.append(rows)
# ##print("length",len(data))
# #txtfile.close()
# ## #写入
# #with open(path,"w",encoding='ascii') as f:
# # 
# #  for i in range(len(data)):
# #      f.writelines(data[i].decode('ascii'))
# 
# file_path=r'C:\Users\administered\Desktop\t.sql'
# path=r'file_sql.sql'
# f=open(file_path,"r",encoding='utf-8')
# ff=open(path,"r")
# f.readline()
# for line in f:
#     lines=line.decode("ascii")
#     ff.write(lines)
# =============================================================================
