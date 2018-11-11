# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import sys

ticks = time.time()

t = time.localtime()



print(ticks)

print(t)


print(time.mktime(t))

print(time.localtime(ticks))



print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1418992496)))

if isinstance("dsf",str):
    print(type("dsf"))
else:
    print("dsf")
    
#sys.exit()
    
if isinstance(23,str):
    print(type(223))
else:
    print(24)
print(65465413215132156)

print(time.strptime('2014-12-19 20:34:56','%Y-%m-%d %H:%M:%S'))

aaa=((1,2,3),(1,2))
print(len(aaa))

    