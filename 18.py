# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:09:25 2021

@author: 123
"""

a = int(input("測試的資料量"))

for i in range (0,a):
    x = input("輸入血型").split(" ")
    if x[0]=="O" and x[1]=="O" and x[2]=="O":
        print("YES")
    elif x[0]=="O" and x[1]=="A" and (x[2]=="O" or x[2]=="A"):
        print("YES")
    elif x[0]=="A" and x[1]=="O" and (x[2]=="O" or x[2]=="A"):
        print("YES")
    elif x[0]=="O" and x[1]=="B" and (x[2]=="B" or x[2]=="O"):
        print("YES")
    elif x[0]=="B" and x[1]=="O" and (x[2]=="B" or x[2]=="O"):
        print("YES")    
    elif x[0]=="O" and x[1]=="AB" and (x[2]=="A" or x[2]=="B"):
        print("YES")
    elif x[0]=="AB" and x[1]=="O" and (x[2]=="A" or x[2]=="B"):
        print("YES")
    elif x[0]=="A" and x[1]=="A" and (x[2]=="A" or x[2]=="O"):
        print("YES")
    elif x[0]=="A" and x[1]=="B" and (x[2]=="A" or x[2]=="B" or x[2]=="O" or x[2]=="AB"):
        print("YES")
    elif x[0]=="B" and x[1]=="A" and (x[2]=="A" or x[2]=="B" or x[2]=="O" or x[2]=="AB"):
        print("YES")
    elif x[0]=="A" and x[1]=="AB" and (x[2]=="A" or x[2]=="B" or x[2]=="AB"):
        print("YES")
    elif x[0]=="AB" and x[1]=="A" and (x[2]=="A" or x[2]=="B" or x[2]=="AB"):
        print("YES")    
    elif x[0]=="B" and x[1]=="B" and (x[2]=="B" or x[2]=="O"):
        print("YES")
    elif x[0]=="B" and x[1]=="AB" and (x[2]=="A" or x[2]=="B" or x[2]=="AB"):
        print("YES")
    elif x[0]=="AB" and x[1]=="B" and (x[2]=="A" or x[2]=="B" or x[2]=="AB"):
        print("YES")O 
    elif x[0]=="AB" and x[1]=="AB" and (x[2]=="A" or x[2]=="B" or x[2]=="AB"):
        print("YES")
    else:
        print("IMPOSSIBLE")