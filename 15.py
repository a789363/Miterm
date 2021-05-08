# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:47:57 2021

@author: 123
"""


n=input("輸入一組四位數字為:")

list1=list(map(int,n))

for i in range(len(list1)):
    
    a=((list1[0]+7)%10)
    b=((list1[1]+7)%10)
    c=((list1[2]+7)%10)
    d=((list1[3]+7)%10)
    
print(str(c)+str(d)+str(a)+str(b))
