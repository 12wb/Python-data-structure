# 水仙花数
# 153 = 1³ + 5³ + 3³。
# 370 = 3³ + 7³ + 0³。
# 371 = 3³ + 7³ + 1³。
# 407 = 4³ + 0³ + 7³。
# (1）水仙花数
# 所谓水仙花数：指一个3位数，其个位数字的立方和等于改数本身，例如153=1³+5³+3³
# 求出100~999之间的水仙花数。
# 算法：比如i
# 百位 a （1）a=i//100  (Python //整除  其它语言/整除）a = int(i/100)   Python
# 十位 b （2）b= (i%100) //100           b = int( (i-100*a)/10)
# 各位 c  （3）c = i %10      c = i-a*100-b*10     c= i-int(i/10)*10
'''
max_num = int(input("请输入求水仙花数的最大范围："))
print("小于", max_num, "的水仙花数有：")
for num in range(100, max_num):
    l = len(str(num))
    str_list = list(str(num))
    num_list = list(map(int, str_list))
    sum = 0
    for i in num_list:
        sum = sum + i ** l
    if sum == num:
        print(num)
    else:
        pass'''



# (2) 计算10000以内的自守数
# 自守数：某个数的平方的末尾数等于这个数
#      eg:5×5=25
#      6×6=26
#      25×25=625
#      76×76=5776
#
# 如果知道n位自守数f为a,那么n+1的自守数应该在a的前面再加一个数。
# 算法：n*n%(10**len(str(n))==n

'''
for i in range(10000):
    if i*i%(10**(len(str(i)))) == i: # 求数的长度以及计算数的后几位
        print(i)'''



# (3)出售金鱼
# 鱼商A将养的一缸金鱼分5次出售，第1次卖出全部的一半加1/2条；第二次卖出余下的三分之一加1/3条；第三次卖出余下的四分之一加1/4条；第四次卖出余下的五分之一加1/5条；最后卖出余下的11条，问原来鱼缸多少条鱼？
# 算法：第j次卖余下的1/(j+1)+(j+1)条
#            假设第j次鱼的总数为x条
#         第一次总鱼： x   x-1/2*x-1/2
#        第二次总鱼： x-1/2*x-1/2      第二次留下的：( x-1/2*x-1/2)-(1/3( x-1/2*x-1/2)+1/3)
#        第j次留下:(x-(x+1)/j+1)条

n = 11
while True:
    x = n
    for i in range(2, 5+1):
        x = x-(x/i+1/i)
    if x == 11:
        print(n)
        x = n
        for i in range(2, 5+1):
            m = x/i+1/i
            x = x - m
            print('%d: mai-->%d shend-->%d' %(i-1, m, x))
        break
    n = n + 1


# 汉诺塔问题
'''
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
# 调用
hanoi(5, 'A', 'B', 'C')'''


# (4)小明有5本书，借给甲乙丙三位小朋友，每人每次只能借一本，有多少种不同借法？
count = 0
for a in range(1,6):
    for b in range(1,6):
        if a!=b:
            for c in range(1,6):
                if c!=a and c!=b:
                    count += 1
                    print(count)

# 2.某天夜里，A，B，C，D，E，五人一起去捕鱼，到第二天凌晨时都疲惫不堪
# 于是各自找地方睡觉，天亮了，A第一个醒来,他将鱼分为五份,把多余的一条鱼扔掉,
# 拿走自己的一份.B第二个醒来,也将鱼分为五份,把多余的一条鱼扔掉,拿走自己的一份.C、D、E依次醒来,
# 按同样的方法拿鱼.问他们伙伴至少捕捉了多少条鱼？（3121）
fish = 1
while 1:
    flag = 1
    total = fish
    for _ in range(5):  # _占位符，表示不在意变量的值，只是用于循环遍历N次，无法打印变量值
        if(total - 1)%5==0:  # % 取余
            total = (total - 1)// 5*4  # // 整除
        else:
            flag = 0
    if flag:
        print(fish)
        break
    fish += 1
