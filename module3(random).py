"""
#random模块
1.seed(x)            初始化给定的随机种子，默认为系统时间
2.random()           产生一个[0.0，1.0)之间的随机小数
3.randint(a,b)       生成一个[a,b]之间的整数
4.randrange(m,n,k)   生成一个[m.n)之间步长为k的随机整数
5.uniform(a,b)       生成一个[a,b]之间的随机小数
6.choice(seq)        从序列中随机选择一个元素
7.shuffle(seq)       将序列seq中的元素随机排列，返回打乱后的序列
"""
import random
random.seed(10)
print(random.random())
print(random.random())

print(random.randint(1,100))

print(random.uniform(1,100))

lst=[i for i in range(10)]
print(random.choice(lst))

random.shuffle(lst)
print(lst)