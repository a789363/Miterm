# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:35:05 2021

@author: 123
"""

team = int(input("組數為"))
ans = []
b = 0
for i  in range(1,team+1):
    a = input("第"+str(i)+"組").split(" ")
    ans.append( int(a[0])*250+int(a[1])*175)
    
for i in ans:
    b += 1
    print("第"+str(b)+"組應收費用:"+str(i))