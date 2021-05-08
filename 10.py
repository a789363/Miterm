# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:24:21 2021

@author: 123
"""
n =1
m = 1
b =""
c = ""
while True:
    a = input("輸入N及M為:").split(" ")
    n = int(a[0])
    m = int(a[1])
    if (n == 0 & m == 0):
        break
    else:
        score=[[0]*m for i in range(n)]
        

      
        for i  in range(0,int(n),1):
            b = input("輸入矩陣數值第"+str(i+1)+"列為").split(" ")
            for j in range(0,int(m),1):
                score[i][j] =b[j]
 
            
        for j in range(0,int(m),1):
            for i  in range(0,int(n),1):
                c = c + score[i][j]+" "
            print("輸出矩陣第",(i+1),"列為",c)
            c =""
        
        
            
                        
