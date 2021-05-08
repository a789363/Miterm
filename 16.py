# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:51:45 2021

@author: 123
"""
n = 0
count = 0
a1 = []
b1 =[]
a2=[]
b2=[]
num1 = []
num2 = []
num3 = []
num4 = []
dic = {'S3':3, 'H3':16, 'C3':42, 'D3':29, 'S4':4, 'H4':17, 'C4':43, 'D4':30, 'S5':5, 'H5':18, 'C5':44, 'D5':31,
       'S6':6, 'H6':19, 'C6':45, 'D6':32, 'S7':7, 'H7':20, 'C7':46, 'D7':33, 'S8':8, 'H8':21, 'C8':47, 'D8':34,
       'S9':9, 'H9':22, 'C9':48, 'D9':35, 'S10':10, 'H10':23, 'C10':49, 'D10':36, 'S11':11, 'H11':24, 'C11':50, 'D11':37,
       'S12':12, 'H12':25, 'C12':51, 'D12':38, 'S13':13, 'H13':26, 'C13':52, 'D13':39, 'S1':1, 'H1':14, 'C1':40, 'D1':27,
       'S2':2, 'H2':15, 'C2':41, 'D2':28}  # 紀錄點數

while (n != -1):
    count = 0
    count1 = 0
    a = input("第一行的牌").split(" ")
    b = input("第二行的牌").split(" ")
    n = int(input("結束字元"))
    for i in a: #紀錄玩家花色點數
        flor = int(dic[i] / 13)+1  #判斷花色
        a1.append(flor)
        point = dic[i] % 13  #判斷點數
        b1.append(point)
    for i in range (len(a1)):
        num1.append(a1.count(a1[i])) #花色次數
        num2.append(b1.count(b1[i])) #點數次數
        b1.sort(reverse=True)
        a1.sort(reverse=True)
        num1.sort(reverse=True)
        num2.sort(reverse=True)    
    for i in b: #紀錄對手花色點數
        flor = int(dic[i] / 13)+1  #判斷花色
        a2.append(flor)
        point = dic[i] % 13  #判斷點數
        b2.append(point)
     
    for i in range (len(a1)):
        num3.append(a2.count(a2[i])) #花色次數
        num4.append(b2.count(b2[i])) #點數次數
        b2.sort(reverse=True)
        a2.sort(reverse=True)
        num3.sort(reverse=True)
        num4.sort(reverse=True)
 
    for i in range(len(a1)):
         if num1[0] < 5: #沒有同花順
            if num2[0] < 4 :#沒有鐵支
                if num2[0] <3: #沒有條或葫蘆
                    if num2[0] < 2: #沒有對
                        if b1[0]-b1[4]==4:
                            count+= 3
                        else:
                            for j in range(len(a1)):  #雜牌的比較
                              if b1[j] > b2[j]:
                                 count +=1 
                    else: #算有幾個對
                        for k in range(len(a1)):
                              if num2[k] == 2:
                                 count += 0.5  
                else: #算看看有沒有葫蘆跟條
                       
                       for k in range(len(a1)):
                             
                          if num2[k] == 3:
      
                              count += 2
                          if num2[k] == 2:
                              count +=1
            else: #算鐵支
                for k in range(len(a1)):
                    if num2[k] == 4:
                        count +=3
         else: #判斷是同花順嗎
                if b1[0]-b1[4] == 4:
                    count += 15
                else:
                    for k in range(len(a1)):
                        if b1[k] > b2[k]:
                            count +=1 
    for i in range(len(a1)):
         if num3[0] < 5: #沒有同花順
            if num4[0] < 4 :#沒有鐵支
                if num4[0] <3: #沒有條或葫蘆
                    if num4[0] < 2: #沒有對
                       if b2[0]-b2[4]==4:
                           count1-= 3
                       else:
                            for j in range(len(a1)):  #雜牌的比較
                              if b2[j] > b1[j]:
                                 count1 -=1 
                    
                    else: #算有幾個對
                        for k in range(len(a1)):
                              if num4[k] == 2:
                                 count1 -= 0.5                       
                else: #算看看有沒有葫蘆跟條
                       for k in range(len(a1)):
                          if num4[k] == 3:
                              count1 -= 2
                          if num4[k] == 2:
                              count1 -=1
            else: #算鐵支
                for k in range(len(a1)):
                    if num4[k] == 4:
                        count1 -=3
         else: #判斷是同花順嗎
                if b2[0]-b2[4] == 4:
                    count1 -= 15
                else:
                    for k in range(len(a1)):
                        if b2[k] > b1[k]:
                            count1 -=1 
            
    if (count+count1) > 0:
        print("1")
    else:
        print("0")
        
        
            
