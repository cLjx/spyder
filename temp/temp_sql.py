# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 19:05:31 2018

@author: administered
"""

import pymysql
import numpy as np
import matplotlib.pyplot as plt

host = 'localhost'
port = 3306
user = 'admin'
passwd = 'admin'
database = 'info'
charset = 'utf8'

connect = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=database,charset=charset)
cursor = connect.cursor();

table="test_table";

sql = 'SELECT * from ' +table;
cursor.execute(sql);

try:
    for row in cursor.fetchall():
        print("id:%d\t a:%d\t b:%d" % row);
except Exception as e:
    connect.rollback()
    print('error\t',e)
        
cursor.close()
connect.close()

plt.figure(1)
x= np.linspace(-np.pi,np.pi,100)
plt.plot(x,np.sin(x))
plt.show()



