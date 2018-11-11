# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:12:10 2018

@author: administered
"""

import mysql.connector
import xlrd

host = 'localhost'
port = 3306
user = 'admin'
passwd = 'admin'
database = 'infog'
charset = 'utf8'

def read_excel_head():
    workbook = xlrd.open_workbook(r'C:\Users\administered\Desktop\SQL数据.xlsx')
    sheet = workbook.sheet_by_name('ods_wei_stations')
    #print(type(sheet.cell_value(17,4).encode('utf-8')))
    #print(sheet.cell_value(0,0).encode('utf-8').decode())
    tempstr=''
    for i in range(68):
        tempstr = ' '+tempstr+sheet.cell_value(i,3).encode('utf-8').decode() +' '+\
                    sheet.cell_value(i,4).encode('utf-8').decode()+' ,'
    tempstr = tempstr[:-1]
    #print(tempstr)
    return tempstr

def read_excel_body(i,j):
#    row=row+2
    workbook = xlrd.open_workbook(r'E:\weicheche\ods_wei_stations.xls')
    sheet = workbook.sheet_by_name('Sheet1')
#    tempstr=''
#    for i in range(43):
#        temp=sheet.cell_value(row,i);
#        print(type(temp))
#        
#        tempstr =' '+tempstr+sheet.cell_value(row,i).encode('utf-8').decode() +' ,'
#    tempstr = tempstr[:-1]
    #print(tempstr)
    return sheet.cell_value(i+5,j).encode('utf-8').decode()

if __name__ == '__main__':
    connect = mysql.connector.connect(host=host,port=port,user=user,passwd=passwd,\
                              db=database,charset=charset)
    cursor = connect.cursor();
    
    #createSQL = 'CREATE TABLE ods_wei_stations ('+ read_excel_head() +')'
    tempshow = 'show tables'
    cursor.execute(tempshow);
    existed = False 
    for row in cursor.fetchall():
        if row[0].__eq__('ods_wei_stations'):
            existed = True
            #print(row[0])
    #print(existed)
    if not existed :
        createSQL = 'CREATE TABLE ods_wei_stations ('+ read_excel_head() +')'
        cursor.execute(createSQL);
        
    tempdelete = 'DELETE FROM ods_wei_stations;'
    cursor.execute(tempdelete);
    connect.commit();
        
    for i in range(1492):
#    for i in [77,78,79,80]:
        addSQL = 'INSERT INTO  ods_wei_stations \
        ( stid, stname, longitude, latitude, real_district, real_city, real_province, \
        real_address )  VALUES (%d,\'%s\',%f,%f,\'%s\',\'%s\',\'%s\',\'%s\')' \
         %(int(read_excel_body(i,0)),read_excel_body(i,9),float(read_excel_body(i,11)),float(read_excel_body(i,12)),read_excel_body(i,13),read_excel_body(i,14),read_excel_body(i,15),read_excel_body(i,16)  )
        
#        print(addSQL)
        cursor.execute(addSQL);
        connect.commit();
        print(i,end=' ')
    
    cursor.close()
    connect.close()
    
    


