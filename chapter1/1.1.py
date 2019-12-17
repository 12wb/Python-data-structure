# 三角形面积
from math import *
a = int(input("请输入no 1:"))
b = int(input("请输入no 2:"))
c = int(input("请输入no 3:"))
if a+b > c and a+c > b and b+c > a:
    p = (a+b+c)/2
    s = sqrt((p-a)*(p-b)*(p-c)*p)
    print(s)
else:
    print("不满足")


    
