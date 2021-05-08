# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:46:18 2021

@author: 123
"""

a=str(input("輸入查詢學號:"))
x=[["123","TOM","DTGD",],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
if a==x[0][0]:
    print( "學生資料為:","123 Tom DTGD")
elif a==x[1][0]:
    print("學生資料為:","456 Cat CSIE")
elif a==x[2][0]:
    print("學生資料為:","789 Nana ASIE")
elif a==x[3][0]: 
    print("學生資料為:","321 Lim DBA")
elif a==x[4][0]: 
    print("學生資料為:","654 Won FDD")
    
