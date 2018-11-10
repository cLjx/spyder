# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:17:37 2018

@author: administered
"""


import pymysql
import numpy as np

import initialization

class mSQL:
    
    def __init__(self):
        mSQL.connect = pymysql.connect(host=initialization.host,port=initialization.port,
                          user=initialization.user,passwd=initialization.passwd,
                          db=initialization.database,charset=initialization.charset)
        mSQL.cursor = mSQL.connect.cursor();

    def close(self):        
        mSQL.cursor.close()
        mSQL.connect.close()

    # 查看分类数据
    def mClassificate(temp,*var):
        #print(var)
        for v in var:
            sql = 'SELECT '+v+', COUNT( '+v + ') as size' +' FROM '+ initialization.table+' GROUP BY ' +v;
            #sql= 'SELECT user_identity_type,COUNT(user_identity_type) as size FROM ods_wei_order_info GROUP BY user_identity_type'
            mSQL.cursor.execute(sql);
            res = []
            for row in mSQL.cursor.fetchall():
                #print(type(row))
                res.append(list(row))
                print('{} : {}'.format(v,row));
            print('')
            resNp = np.array(res)
            resNp_ = np.true_divide(resNp[:,2],np.linspace(sum(resNp[:,2]),sum(resNp[:,2]),resNp.dim)
            print(resNp_)
            


if __name__ == '__main__':
    m = mSQL();
    m.mClassificate("user_identity_type","pay_status");
    m.close();