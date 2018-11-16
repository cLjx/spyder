# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:40:52 2018

@author: administered
"""
import pandas as pd, numpy as np
import os ,time
from pyecharts import Bar, Line, Grid ,Bar3D , Geo ,Pie
import mSQLFunction


printO = {'w':'周','M':'月','Q':'季','B':'工作日','D':'日'}

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
#    print(alldf.columns)
    data = 0
    tempii = -1
    for tempi in minit['type']:
        tempii += 1
        if tempii == 0:
            alldfOut = alldf[alldf['goods_name'] == tempi]
        else:
            alldfOut = pd.concat([alldfOut,alldf[alldf['goods_name'] == tempi]])
    if not tempii == -1 :
        alldf = alldfOut
#    alldf = alldf[alldf['goods_name'] in minit['type']]
    dftype = alldf.to_period(minit['axis'])
#    print(dftype.head())
    df_ = pd.pivot_table(dftype,index=['date','goods_name'],
                   values=['subtotal','actual_price'], # 前面是goods_number
                   aggfunc = [len,np.min,np.median,np.sum])
#        df_ = pd.pivot_table(dftype,index=['date','goods_name'],
#                       values=['goods_number'],
#                       aggfunc = [len,np.min,np.median,np.max])
#        print(df_.head(10))
#        print(dftype.head())
#    print(minit['axis'])

    alldfT = alldf[['num','subtotal']].resample(minit['axis']).sum().to_period(minit['axis'])
    print('{} 条 ---> {} {}数据'.format(alldf['num'].sum(),len(alldfT),printO[minit['axis']]))
    
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
    dataProfit = mydraw(minit)
    mydraw_(minit)
    return pd.read_csv('csv_temp/mAllT alldfT.csv')

def mydraw(minit):
    line_subtotal = Line(printO[minit['axis']]+'：总收益（分）',title_pos="65%")
#    data_line_subtotal = list(alldfT['subtotal'])
    data_line_subtotal = list(pd.read_csv('csv_temp/mAllT alldfT.csv')['subtotal'])
    attr_line_subtotal = list(pd.read_csv('csv_temp/mAllT alldfT.csv')['date'])
#    print(attr_line_subtotal[1:5])
#    print(data_line_subtotal[1:5])
    line_subtotal.add('收益',
             attr_line_subtotal,
             data_line_subtotal,
             legend_pos="80%",
             is_datazoom_show=True,
             datazoom_type="inside",
#             xaxis_interval=0, xaxis_rotate=30,
             )

    line_num = Line('周：总订单个数')
#    data_line_num = list(alldfT['num'])
    data_line_num = list(pd.read_csv('csv_temp/mAllT alldfT.csv')['num'])
    attr_line_num = list(pd.read_csv('csv_temp/mAllT alldfT.csv')['date'])
#    print(attr_line_subtotal[1:5])
#    print(data_line_subtotal[1:5])
    line_num.add('订单个数',
             attr_line_num,
             data_line_num,
             legend_pos="20%",
             is_datazoom_show=True,
             datazoom_type="inside",
             )
    
    grid = Grid(height = 800, width = 1600)
#    grid.add(line_subtotal, grid_bottom="60%", grid_left="60%")
#    grid.add(line_num, grid_bottom="60%", grid_right="60%")
    
    grid.add(line_subtotal, grid_bottom="20%", grid_left="10%")
    grid.add(line_num, grid_bottom="20%", grid_left="10%")
    grid.render('img-收益和订单数.html')
    return {'attr':attr_line_subtotal,'value':data_line_subtotal}
    
def mydraw_(minit):
    df_temp = pd.read_csv('csv_temp/mAllT df_.csv')
    #price number
    df_temp.columns = ['date','goods_name','len_p','len_n','min_p','min_n','m_p','m_n','sum_p','sum_n']
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
    df_for_add = df_for_add['no_use'].resample(minit['axis']).sum().to_period(minit['axis'])
    
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
    def get_x_d(df,df_for_add,aim):
        y=-1
        ddd=np.array([0, 0 ,0])
        for i in df_goods_name:
            y += 1
#            print(i)
            df_for = df[df['goods_name'] == i]                     
            dff = pd.merge(df_for_add,df_for,on='date',how = 'left')
            dff = dff.fillna(0)
            d3 = for_add(dff[aim])
            d3 = np.array(d3)
            d1 = np.transpose(np.array([y for yy in range(d3.shape[0])]))        
            ddd = np.vstack((ddd,np.column_stack((d3,d1))))
        ddd = np.delete(ddd,0,axis=0)
        return {'x':list(df_for_add['date']),'d':ddd}
    
#    x_axis = list(df_for_add['date'])
    get_x_d_r = get_x_d(df,df_for_add,'len_n')
    x_axis = get_x_d_r['x']
    ddd = get_x_d_r['d']
    y_axis = df_goods_name
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    sub_title = str(list(df_goods_name))
    
    maxRange = max(ddd[:,1])
    bar3d_n = Bar3D("各种油的订单量",subtitle=sub_title, width=1600, height=800)
    bar3d_n.add(
    "",
    x_axis,
    y_axis,
    [[d[0], d[2], d[1]] for d in ddd],
    is_visualmap=True,
    visual_range=[0, maxRange],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    )
    bar3d_n.render('img-各种油的订单量.html')
    
    get_x_d_r = get_x_d(df,df_for_add,'m_p')
    x_axis = get_x_d_r['x']
    ddd = get_x_d_r['d']
    ddd[:,1] = ddd[:,1]-60000
    ddd = np.maximum(ddd, 0)
#    print(ddd)
    y_axis = df_goods_name
    maxRange = max(ddd[:,1])
    bar3d_m = Bar3D("各种油的平均价格 = ( Z + 60,000 ) 分/毫升 ",subtitle=sub_title, width=1600, height=600)
    bar3d_m.add(
    "",
    x_axis,
    y_axis,
    [[d[0], d[2], d[1]] for d in ddd],
    is_visualmap=True,
    visual_range=[0, maxRange],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    )
    bar3d_m.render('img-各种油的平均价格.html')

    
    get_x_d_r = get_x_d(df,df_for_add,'sum_n')
    x_axis = get_x_d_r['x']
    ddd = get_x_d_r['d']
    ddd[:,1] = ddd[:,1]/1000000
    ddd = np.maximum(ddd, 0)
#    print(ddd)
    y_axis = df_goods_name
    maxRange = max(ddd[:,1])
    bar3d_m = Bar3D("各种油的收益 （万元）",subtitle=sub_title, width=1600, height=600)
    bar3d_m.add(
    "",
    x_axis,
    y_axis,
    [[d[0], d[2], d[1]] for d in ddd],
    is_visualmap=True,
    visual_range=[0, maxRange],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    )
    bar3d_m.render('img-各种油的收益.html')
    
    
def mGeoAll(df,minit):
    df.dropna(axis=0, how='any', inplace=True)
    print(df.head())
    attr = list(df['city'])
    value = list(df['count'])
    
    geo = Geo(
            "全国油站数量分布",
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59",
            )
    range_max = max(value)
    geo.add(
            "",
            attr,
            value,
            visual_range=[0, range_max],
            visual_text_color="#fff",
#            symbol_size=15,
            is_visualmap=True,
            )
    geo.render('全国油站数量分布.html')
    
    
def mDrawMulti(multi,minit):
    line = Line('',height = 600, width = 1600)
    time_s = time.strftime('%Y-%m-%d',time.strptime(minit['s'],'%Y-%m-%d %H-%M-%S'))
    time_e = time.strftime('%Y-%m-%d',time.strptime(minit['e'],'%Y-%m-%d %H-%M-%S'))
    temp_index = pd.date_range(start=time_s,end=time_e)
    df_for_add = pd.DataFrame(np.zeros(len(temp_index)),index = temp_index)
    df_for_add.columns = ['no_use']
    df_for_add = df_for_add['no_use'].resample(minit['axis']).sum().to_period(minit['axis'])
    def for_add(x):
        open('csv_temp/no-use.csv','w').close()
        x.to_csv('csv_temp/no-use.csv',index = True , header = True)
        x = pd.read_csv('csv_temp/no-use.csv')
        os.remove('csv_temp/no-use.csv')
        return x
    df_for_add = for_add(df_for_add)
    df_for_add.columns = ['date','no_use']
    def get_x_d(df,df_for_add):            
        dff = pd.merge(df_for_add,df,on='date',how = 'left')
        dff = dff.fillna(0)
        return dff
    df = get_x_d(multi[0]['df'],df_for_add)
    def mwrite(df):
        open('csv_temp/-------------------.csv','w').close()
        df.to_csv('csv_temp//-------------------.csv',index = True , header = True)
#    mwrite(df)
    attr = list(df['date'])
    for sample in multi:
        title = str(sample['st'])
        df = sample['df']
        df.columns = ['date','num','subtotal']
        value = list(get_x_d(df,df_for_add)['subtotal'])
        line.add(title,attr,value,mark_line=["average"],is_datazoom_show=True,datazoom_type="inside",)
        
    line.render('img-好几个油站的总收益.html')
    
    
def mCityAll(dfAll,minit):
    df_ = dfAll.drop('id',axis=1).groupby('city').agg([len])
    attr = list(df_.index)
    value = list(df_['count']['len'])
    pie = Pie("")
    pie.add(
        "各个城市的油站数量",
        attr,
        value,
        is_random=True,
        rosetype="area",
        is_legend_show=False,
        is_label_show=True,
        legend_pos="20%",
    )
    pie.render('img-各个城市的油站数量.html')
#    print(dfAll)
    
    df = dfAll[dfAll['city'] == minit['st']]
    list_id = list(df['id'])
    return list_id

#    mm = mSQLFunction.mSQL()    
#    multi = []
#    for i in list_id:
#        minit['st'] = i
#        temp = mAll(mm.mAll(minit),minit)
#    #    multi.append({'st':i, 'attr':temp['attr'], 'value':temp['value']})
#        multi.append({'st':i, 'df':temp})
#    mDrawMulti(multi,minit)
#    mm.close()
    
    
    
    
    
    
    
    
    

    
