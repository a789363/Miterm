# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:06:26 2021

@author: 123
"""

n = int(input("輸入第一行正整數"))

n1 = input("輸入第二行數列中的數字為:").split(",")

list1 = []

for i in range(n):
    sum1 = n1[i]
    cont = n1.count(sum1)
    list1.append(cont)
b = max(list1)
c = list1.index(b)
count = 0
for i in range(len(list1)):
    if b ==list1[i]:
        count +=1
if count > b:
    print("數字剛好出現"+str(b)+"次")
else:
    print("出現最多的數字是",n1[c])
    print("出現的次數是",b)

    
