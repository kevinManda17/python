#coding:utf-8
import datetime 

d1=datetime.date(2023,8,18, 16,1,42)
d2=datetime.datetime(2023,8,17,16,1,42)

if d1 <d2 :
    print("d1 est plus ancien que d2")
else:
    print("d1 est plus recent que d2")

#coding:utf-8
# from datetime import datetime
# 
# print(datetime.now())