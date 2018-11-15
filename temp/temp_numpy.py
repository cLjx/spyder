# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:47:11 2018

@author: administered
"""

# =============================================================================
# #python数据分析之numpy学习
# =============================================================================

# =============================================================================
# 数组的创建
# =============================================================================

import numpy as np

ls1 = range(10)

print(ls1)

print(list(ls1))

print(type(ls1))

ls2 = np.arange(10)

print(ls2)

print(list(ls2))

print(type(ls2))

arr1 = np.array((10,11,12,14,15))

print(arr1)

arr2 = np.array([1,2,3,6,9])

print(arr2)

print(np.ones([3,4]))

a = np.ones([2,3])

print(a)

print(a.ravel())

print(np.ones([2,3]).ravel())












