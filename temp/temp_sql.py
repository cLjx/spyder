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
database = 'infog'
charset = 'utf8'

connect = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=database,charset=charset)
cursor = connect.cursor();


sql = 'SELECT mst.stid , mst.real_city , minfo.create_time FROM ods_wei_stations as mst, ods_wei_order_info as minfo WHERE mst.stid = 10277 AND minfo.create_time < 1418735210 ;';
cursor.execute(sql);

try:
    for row in cursor.fetchall():
        print(row);
except Exception as e:
    print('error\t',e)
        
cursor.close()
connect.close()

plt.figure(1)
x= np.linspace(-np.pi,np.pi,100)
plt.plot(x,np.sin(x))
plt.show()



