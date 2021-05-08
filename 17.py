# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:51:44 2021

@author: 123
"""

dict1 = {"A":1,"J":11,"Q":12,"K":13,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
ans = 0
a = input("請輸入卡牌").split(" ")

for i in range (len(a)):
    ans = dict1[a[i]] + ans
    

print(ans)