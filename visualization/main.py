# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:26:29 2018

@author: administered
"""
import pandas as pd
import mSQLFunction, mPlot

#st可以是油站的id（stid）,例如st=10387;或者油站名字（stname），例如st='中海油华英加油站'
m_st=10314
#查看方式,年：'Y'，月：'M'，日：'D'，时：'H'，周：'W'
m_axis='W'
#时间段，起始,格式：'2014-06-20 00-00-00'
m_time_s='2015-06-10 00-00-00'
#时间段，截至，格式：'2014-09-18 00-00-00'
m_time_e='2018-09-18 00-00-00'
#商品类型: 10. 油品 20. 非油品 30. 团购 40. 闪付
m_type=10



minit={'st':m_st,'axis':m_axis,'s':m_time_s,'e':m_time_e,'type':m_type}

m = mSQLFunction.mSQL()

#dfS = m.mStTiPro(minit)

#dfT = m.mTi(minit)

mPlot.mAll(m.mAll(minit),minit)




m.close()






