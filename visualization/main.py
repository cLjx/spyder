# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:26:29 2018

@author: administered
"""
import pandas as pd
import mSQLFunction, mPlot

#st可以是油站的id（stid）,例如st=10387;或者油站名字（stname），例如st='中海油华英加油站'
m_st=10314
#查看方式,月：'M'，周：'w'，季度：'Q',工作日：'B',每一天：'D'
m_axis='D'
#时间段，起始,格式：'2014-06-20 00-00-00'
m_time_s='2014-08-13 00-00-00'
#时间段，截至，格式：'2014-09-18 00-00-00'
m_time_e='2016-09-18 00-00-00'
#商品类型:
#['oil0', 'oil93', 'oil97', 'oil98', 
# '京五0#普通柴油', '京五0#车用柴油', '京五92#汽油', '京五95#汽油', 
# '国五0#农机柴油', '国五0#普通柴油', '国五0#车用柴油', '国五89#车用汽油', 
# '国五92#车用汽油', '国五95#车用汽油', '国五98#车用汽油', '国六92#车用汽油',
# '国四0#车用柴油', '国四90#车用汽油', '国四93#车用汽油', '国四97#车用汽油', 
# '沪五0#车用柴油', '沪五92#汽油', '沪五95#汽油']
m_type=[]



minit={'st':m_st,'axis':m_axis,'s':m_time_s,'e':m_time_e,'type':m_type}

m = mSQLFunction.mSQL()

#dfS = m.mStTiPro(minit)

#dfT = m.mTi(minit)

mPlot.mAll(m.mAll(minit),minit)

#mPlot.mGeoAll(m.mGeoAll(minit),minit)


m.close()






