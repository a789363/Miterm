# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:57:26 2021

@author: 123
"""

x= input("輸入查詢組數N為:")
acc = [[123,456,9000],[456,789,5000],[789,888,6000],[336,558,10000],[775,666,12000],[566,221,7000],[0,0,"error"]]
ans =[]
count = 0
for k in range(0,int(x)):
    a = input("輸入帳號密碼").split(" ")
    for i in range(0,6):
        if int(a[0]) == acc[i][0]and int(a[1]) == acc[i][1]:
            ans.append(i)
            break
        else:
            count +=1
            if count ==5:
                ans.append(6)
for i in ans:
    print(acc[i][2])