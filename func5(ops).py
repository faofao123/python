"""
常用内置函数
1.数据类型转换函数
bool(obj)获取指定对象obj的布尔值
str(obj)
int(x)
float(x)
list(sequence)
tuple(sequence)
set(sequence)

"""

lst=[1,2,3,4,5,6,7,8,9]
print(type(lst),lst)
s=str(lst)
print(type(s),s)

print(int(10.2)+int('8'))#错误类型：int('a')  int('0.8')

print(float(0.8)+float(10.2))

s='hello'
print(list(s))

seq=range(10)
print(list(seq))
print(tuple(seq))
print(set(seq))
#——————————————————————————————————————————————————————————————
"""
2.数学函数
abs(x)         绝对值
divmod(x,y)    获取x与y的商和余数
max(sequence)  最大值
min(sequence)  最小值
sum(iter)      对可迭代对象求和
pow(x,y)       获取x的y次幂
round(x,d)     对x进行保留d位小数，结果四舍五入
"""
print(abs(-10),abs(-1.2),abs(0))
print(divmod(13,4))
s=divmod(15,4)
print(s[0],s[1])
print(max([1,2,3]))
print(sum([1,2,3,4,5,6,7,8,9]))
print(sum((1,2,3,4,5,6,7,8,9)))
print(pow(2,10))
print(round(3.9415926))#不写后面的参数，保留整数
print(round(3.1415926,3))
print(round(123.45,-1))#参数为负数，小数点前保留
print(round(125.5,-1))
print(round(195.5,-2))
#——————————————————————————————————————————————————————————————
"""
3.迭代器操作函数
sorted(iter)对可迭代对象排序
reversed(sequence)反转序列生成新的迭代器对象
zip(iter1,iter2)将iter1和iter2打包成元组并返回一个可迭代的zip对象
enumerate(iter)根据iter对象创建一个enumaerate对象
all(iter)判断可迭代对象iter中所有元素的布尔值是否都为True(都为true才为true)
any(iter)判断可迭代对象iter中所有元素的布尔值是否都为False(都为false才为false)
next(iter)获取迭代器的下一个元素
filter(funtion,iter)通过指定条件过滤序列并返回一个迭代器对象
map(funtion,iter)通过函数funtion对可迭代对象iter的操作返回一个迭代器对象
"""
lst=[12,5,8,1,9]
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print(asc_lst)
print(desc_lst)

new_lst=reversed(lst)#结果需要转换才能看到
print(list(new_lst))

x=[1,2,3,4]
y=['a','b','c','d','e']
zipobj=zip(x,y)#结果需要转换才能看到
print(list(zipobj))

enum=enumerate(y,start=0)#结果需要转换才能看到
#print(list(enum))

lst2=['',1,2]
print(all(lst2))
print(all(lst))
print(any(lst2))
print(any(lst))

print(next(enum))
print(next(enum))
print(next(enum))

def fun(num):
    return num%2==0#偶数为true
obj=filter(fun,range(10))
print(type(obj))
print(list(obj))

def upper(c):
    return c.upper()
lst3=['hello','world']
new_lst3=map(upper,lst3)
print(type(new_lst3))
print(list(new_lst3))
#——————————————————————————————————————————————————————————————
"""
4.其他函数（看看就行）
len(s)
type(x)
eval(s)
id(s)
format(value,format_spec)
"""
print(format(3.14,'20'))#数值型默认右对齐
print(format('hello','20'))#字符串型默认左对齐
print(format('hello','*>20'))
print(format('hello','*^20'))
