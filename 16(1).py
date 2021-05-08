# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 22:35:34 2021

@author: 123
"""

a = input("幾乘幾").split(" ")

x1=[[0]*int(a[1]) for i in range(int(a[0]))]

for k in range (0,len(a)):
   a1 =input("第一個矩陣第一列的值").split(" ")
   x1.append(a1)
b = input("幾乘幾").split(" ")
x2=[[0]*int(b[1]) for i in range(int(b[0]))]
for k in range (0,len(a)):
   a2 =input("第一個矩陣第二列的值").split(" ")
   x2.append(a2)
        


if a[0] != b[0] or b[1] != b[1]:
    print("不能相加")
    
else:
    for i in range(int(a[0])):

        for j in range(int(a[1])):
            x1[i][j]=int(x1[i][j])+int(x2[i][j])
            
print(x1)
            