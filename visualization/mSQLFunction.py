# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:17:37 2018

@author: administered
"""


import pymysql
import numpy as np
import sys
import time

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
                #print('{} : {}'.format(v,row));
            print('')
            resNp = np.array(res)
            resNp_ = np.true_divide(resNp[:,1],np.linspace(sum(resNp[:,1]),sum(resNp[:,1]),resNp.shape[0]))
            resNp=np.column_stack((resNp,resNp_))
            for i in range(resNp.shape[0]):
                print('{} : {} \t{} \t{:.4}'.format(v,resNp[i,0],resNp[i,1],resNp[i,2]))


#SELECT mst.stid , mst.stname, mst.real_province ,mst.real_city ,mst.real_district ,mst.real_address , 
# mst.longitude , mst.latitude , minfo.user_id , minfo.platform , mit.create_time  
#FROM ods_wei_stations as mst, ods_wei_order_info  as minfo ,ods_wei_order_items as mit 
#WHERE  mst.stid = 10312  AND minfo.merchant_id = mst.stid AND mit.id = minfo.id 
#AND mit.create_time >= 1497888000 AND mit.create_time <= 1537200000 
#ORDER BY mit.create_time;

    #油站 时间 商品
    def mStTiPro(self,minit):
        if isinstance(minit['st'],int):
            sql_st=' mst.stid = '+ str(minit['st'])+' '
        elif isinstance(minit['st'],str):
            sql_st=' mst.stname = \''+ minit['st']+'\' '
        else:
            print(type(minit['st']))
            sys.exit()
        #print(sql_st)
        temp_time_struct = time.strptime(minit['s'],'%Y-%m-%d %H:%M:%S')
        time_s = str(int(time.mktime(temp_time_struct)))
        temp_time_struct = time.strptime(minit['e'],'%Y-%m-%d %H:%M:%S')
        time_e = str(int(time.mktime(temp_time_struct)))
        msql = 'SELECT mst.stid , mst.stname, mst.real_province ,mst.real_city ,mst.real_district ,mst.real_address , \
            mst.longitude , mst.latitude , minfo.user_id , minfo.platform , mit.create_time \
            FROM ods_wei_stations as mst, ods_wei_order_info  as minfo ,ods_wei_order_items as mit  \
            WHERE '+ sql_st +' AND minfo.merchant_id = mst.stid AND mit.id = minfo.id \
            AND mit.create_time >= '+time_s+' AND mit.create_time <= '+time_e+' \
            ORDER BY mit.create_time;'
#        print(msql)
        mSQL.cursor.execute(msql)
        res = mSQL.cursor.fetchall()
        print('共检索到 {} 条数据'.format(len(res)))
        print(res[1:5])
        
        

if __name__ == '__main__':
    m = mSQL();
#    m.mClassificate("goods_type");
    m.close();