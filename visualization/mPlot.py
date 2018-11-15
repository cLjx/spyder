# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:40:52 2018

@author: administered
"""
import pandas as pd, numpy as np
import os ,time
from pyecharts import Bar, Line, Grid ,Bar3D

def mStTiPro(info,df_):
    print(info)
    print('df_ len:{}条'.format(len(df_)))
    print(df_.head())
    
    df = pd.pivot_table(df_,index = ['Y','m','d','H','w'],values=['M'],aggfunc=len)
    print('df len:{}条'.format(len(df)))
    
    def fun_file():
        if not os.path.exists('csv_temp'):
            os.makedirs('csv_temp')

        if os.path.exists('csv_temp/plot_StTiPro.csv'):
            os.remove('csv_temp/plot_StTiPro.csv')
        file1 = open('csv_temp/plot_StTiPro.csv','w')
        file1.close()
        
    fun_file()
    df.to_csv('csv_temp/plot_StTiPro.csv',index = True , header = True)
    
    print(pd.read_csv('csv_temp/plot_StTiPro.csv').head())
    
    return df
    
    
def mTi(df_):
    print('df_ len:{}条'.format(len(df_)))
    print('df_ sum count:{}条'.format(df_.loc[:,['count']].sum()[0]))
#    print(df_.head())
    
    df = df_.sort_values(by = ['count'],ascending = False)
    print(df.head())
    
    def fun_file():
        if not os.path.exists('csv_temp'):
            os.makedirs('csv_temp')

        if os.path.exists('csv_temp/plot_Ti.csv'):
            os.remove('csv_temp/plot_Ti.csv')
        file1 = open('csv_temp/plot_Ti.csv','w')
        file1.close()
        
    fun_file()
    df.to_csv('csv_temp/plot_Ti.csv',index = False , header = True)
    
#    print(pd.read_csv('csv_temp/plot_Ti.csv').head())
    
    return df


def mAll(alldf,minit):
    print('总共:{}条'.format(len(alldf)))
    print(alldf.head())
    print(alldf.columns)
    data = 0
    if minit['axis'] == 'Y' :
        alldfT = pd.pivot_table(alldf,index = ['Y'],values=['M'],aggfunc=len)
        print('共 : {} 年数据'.format(len(alldfT)))
#        alldfT.plot(x='Y',y='M')
    elif minit['axis'] == 'M' :
        alldfT = pd.pivot_table(alldf,index = ['Y','m'],values=['M'],aggfunc=len)
        print('共 : {} 月数据'.format(len(alldfT)))
    elif minit['axis'] == 'D' :
        alldfT = pd.pivot_table(alldf,index = ['Y','m','yday'],values=['M'],aggfunc=len)
        print('共 : {} 日数据'.format(len(alldfT)))
    elif minit['axis'] == 'H' :
        alldfT = pd.pivot_table(alldf,index = ['Y','m','d','H'],values=['M'],aggfunc=len)
        print('共 : {} h数据'.format(len(alldfT)))
    elif minit['axis'] == 'W' :
#        print(alldf[['num','subtotal']].head())
        dftype = alldf.to_period('w')
        print(dftype.head())
        df_ = pd.pivot_table(dftype,index=['date','goods_name'],
                       values=['goods_number','actual_price'],
                       aggfunc = [len,np.min,np.median,np.max])
#        df_ = pd.pivot_table(dftype,index=['date','goods_name'],
#                       values=['goods_number'],
#                       aggfunc = [len,np.min,np.median,np.max])
#        print(df_.head(10))
#        print(dftype.head())
        alldfT = dftype[['num','subtotal']].resample('w').sum()
        print('{} 条 ---> {} 周数据'.format(alldf['num'].sum(),len(alldfT)))
    else:
        print('input type error')
        return 'input type error'
    
    def fun_file():
        if not os.path.exists('csv_temp'):
            os.makedirs('csv_temp')

        if os.path.exists('csv_temp/mAllT df_.csv'):
            os.remove('csv_temp/mAllT df_.csv')
        file1 = open('csv_temp/mAllT df_.csv','w')
        file1.close()
        
        if os.path.exists('csv_temp/mAllT df.csv'):
            os.remove('csv_temp/mAllT df.csv')
        file1 = open('csv_temp/mAllT df.csv','w')
        file1.close()
        
        if os.path.exists('csv_temp/mAllT alldfT.csv'):
            os.remove('csv_temp/mAllT alldfT.csv')
        file1 = open('csv_temp/mAllT alldfT.csv','w')
        file1.close()
        
    fun_file()
    df_.to_csv('csv_temp/mAllT df_.csv',index = True , header = True)
#    df_.to_csv('csv_temp/mAllT df.csv',index = True , header = True)
    alldfT.to_csv('csv_temp/mAllT alldfT.csv',index = True , header = True)
    
#    print(pd.read_csv('csv_temp/mAllT df_.csv').head())
    print(pd.read_csv('csv_temp/mAllT alldfT.csv').head())
    mydraw(minit,alldfT)
    mydraw_(minit)
    return data

def mydraw(minit,alldfT):
    if minit['axis'] == 'W' :
        line_subtotal = Line('周：总收益（分）',title_pos="65%")
    data_line_subtotal = list(alldfT['subtotal'])
    attr_line_subtotal = list(pd.read_csv('csv_temp/mAllT alldfT.csv')['date'])
#    print(attr_line_subtotal[1:5])
#    print(data_line_subtotal[1:5])
    line_subtotal.add('收益',
             attr_line_subtotal,
             data_line_subtotal,
             legend_pos="80%",)
    
    line_num = Line('周：总订单个数')
    data_line_num = list(alldfT['num'])
    attr_line_num = list(pd.read_csv('csv_temp/mAllT alldfT.csv')['date'])
#    print(attr_line_subtotal[1:5])
#    print(data_line_subtotal[1:5])
    line_num.add('订单个数',
             attr_line_num,
             data_line_num,
             legend_pos="20%",)
    
    
    
    grid = Grid(height = 720, width = 1200)
    grid.add(line_subtotal, grid_bottom="60%", grid_left="60%")
    grid.add(line_num, grid_bottom="60%", grid_right="60%")
    
    grid.add(line_subtotal, grid_top="60%", grid_right="20%")
    grid.add(line_num, grid_top="60%", grid_right="20%")
    grid.render('img-收益和订单数.html')
    
    
def mydraw_(minit):
    df_temp = pd.read_csv('csv_temp/mAllT df_.csv')
    #price number
    df_temp.columns = ['date','goods_name','len_p','len_n','min_p','min_n','m_p','m_n','max_p','min_n']
    t = df_temp.drop([0,1]) 
    t.to_csv('csv_temp/mAllT df.csv',index = False , header = True)
    df = pd.read_csv('csv_temp/mAllT df.csv')
#    print(df.head())
#    print(df[df['goods_name'] == 'oil0'].to_period('w').head(10))
    time_s = time.strftime('%Y-%m-%d',time.strptime(minit['s'],'%Y-%m-%d %H-%M-%S'))
    time_e = time.strftime('%Y-%m-%d',time.strptime(minit['e'],'%Y-%m-%d %H-%M-%S'))
    temp_index = pd.date_range(start=time_s,end=time_e)
#    print(len(temp_index))
    df_for_add = pd.DataFrame(np.zeros(len(temp_index)),index = temp_index)
    df_for_add.columns = ['no_use']
    df_for_add = df_for_add['no_use'].resample('w').sum().to_period('w')
    
#    print(df_for_add.head(5))
    
    def for_add(x):
        open('csv_temp/no-use.csv','w').close()
        x.to_csv('csv_temp/no-use.csv',index = True , header = True)
        x = pd.read_csv('csv_temp/no-use.csv')
        os.remove('csv_temp/no-use.csv')
        return x
        
    df_for_add = for_add(df_for_add)
    df_for_add.columns = ['date','no_use']
    
    df_goods_name = list(set(list(df['goods_name'])))
    df_goods_name.sort()
#    print(len(df_goods_name))
    print(df_goods_name)
    y=-1
    ddd=np.array([0, 0 ,0])
    for i in df_goods_name:
        y += 1
        print(i)
        df_for = df[df['goods_name'] == i]
    #    print(df_for_add.head(10))
    #    print(df_for.head(10))
                    
        dff = pd.merge(df_for_add,df_for,on='date',how = 'left')
        dff = dff.fillna(0)
        d3 = for_add(dff['len_n'])
        d3 = np.array(d3)
        d1 = np.transpose(np.array([y for yy in range(d3.shape[0])]))        
        ddd = np.vstack((ddd,np.column_stack((d3,d1))))
#        print(ddd)
    
    print(ddd)
    ddd = np.delete(ddd,0,axis=0)
    x_axis = list(df_for_add['date'])
#    print(x_axis)
    y_axis = df_goods_name
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d = Bar3D("各种油的销量", width=1400, height=800)
    bar3d.add(
    "",
    x_axis,
    y_axis,
    [[d[0], d[2], d[1]] for d in ddd],
    is_visualmap=True,
#    visual_range=[0, 20],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    )
    bar3d.render('img-各种油的销量.html')
    
#    if os.path.exists('csv_temp/mAllT -------.csv'):
#            os.remove('csv_temp/mAllT -------.csv')
#    open('csv_temp/mAllT -------.csv','w').close()
#    df.to_csv('csv_temp/mAllT -------.csv',index = True , header = True)
    
    
    
    
    
    
    
    
    
    

    
