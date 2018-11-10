# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:06:32 2018

@author: administered
"""

import requests as re

url="https://m.amap.com/around/?locations=116.470098,39.992838&keywords=路口&defaultIndex=3&defaultView=&searchRadius=5000&key=35e992dc86d0481451155044429c203d"

url2="http://m.amap.com/around/?locations=116.470098,39.992838&keywords=路口&defaultIndex=3&defaultView=&searchRadius=5000&key=d3f5d8b3b05231fa6a11375492310e3a&platform=mobile";

req = re.get(url2).text

print(req.decoding)

r=req.decode('utf-8');

print(r)