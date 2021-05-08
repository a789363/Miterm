# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:59:03 2021

@author: 123
"""

sum1 = input("輸入月租費形式及通花時間為:").split(",")


a=int(sum1[0])
b=int(sum1[1])
if a==186:
    if b*0.09*2>a:
        print("通話費為:"+str(int(round(b*0.09*0.8,0))))
    elif b*0.09*2<=a:
        print("通話費為:"+str(int(round(b*0.09*0.9,0))))
elif a==386:
    if b*0.08*2>a:
        print("通話費為:"+str(int(round(b*0.08*0.7,0))))
    elif b*0.08*2<=a:
        print("通話費為:"+str(int(round(b*0.08*0.8,0))))
elif a==586:
    if b*0.07*2>a:
        print("通話費為:"+str(int(round(b*0.07*0.6,0))))
    elif b*0.07*2<=a:
        print("通話費為:"+str(int(round(b*0.07*0.7,0))))
elif a==986:
    if b*0.06*2>a:
        print("通話費為:"+str(int(round(b*0.06*0.5,0))))
    elif b*0.07*2<=a:
        print("通話費為:"+str(int(round(b*0.06*0.6,0))))
else:
    print("沒有這個月租費型式")