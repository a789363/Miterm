# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:31:18 2021

@author: 123
"""

a = input("輸入一整數序列為:").split(" ")
count = []
ans= ""
for i in range(len(a)):
    count.append (a.count(a[i]))
    if count[i] > len(a)/2:
        ans = ans + a[i] +" "
        break
    else:
        ans = "NO"
print("過半元數為",ans)
