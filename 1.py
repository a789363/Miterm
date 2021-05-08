# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a =  input("請輸入一個數字")
b = ""
ans = 0

for i in range (len(a)):
    b = a[i::1]
    for k in range(len(b)):
        n = int(b)/(10**k)
        for j in range(2,int(n)):
            if (int(n)%j)==0:
                break
        else:
            if int(n)> ans :
                ans = int(n)
            
if ans == 0:
   print("子陣列最大的值為 : No prime found")
else:
    
    print("子陣列最大的質數值為",ans)        
    

  