# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 20:38:42 2018

@author: administered
"""

from pyecharts import Bar 

bar = Bar('我的第一个图表','这里是副标题')
kwargs = dict(
    name = '柱形图',
    x_axis = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'],
    y_axis = [5,20,36,10,75,90]
)
bar.add(**kwargs)
bar.render('bar01.html')


