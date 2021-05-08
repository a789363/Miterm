# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:40:43 2021

@author: 123
"""

a =  input("輸入值為:").split(",")

a.sort()
b= list(reversed(a))
x1 =""
x2 =""

for i in range(len(a)):
    x1 = x1+a[i]
    x2 = x2+b[i]
    
print( "最大值數列與最小值數列差值為:",(int(x2)-int(x1)))
