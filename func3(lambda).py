"""
#变量的作用域
1.局部变量  仅在函数内部作用
2.全局变量  作用在整个程序
两者重名时，局部变量优先级高

"""
def fun(a,b):
    global s    #global关键字声明为全局变量
    s=10        #赋值和声明必须要分开
    return s+a+b
print(fun(1,2))
print(s)

#匿名函数lambda
#指没有名字的函数，只能使用一次
#result=lambda 参数列表:表达式
s=lambda a,b:a+b
print(type(s))
print(s(1,2))

lst=[1,2,3,4]
for i in lst:
    result=lambda x:i
    print(result(lst),end=' ')
print()
for i in range(len(lst)):
    result=lambda x:x[i]
    print(result(lst),end=' ')
print()

#对列表排序，排序的规则是字典中的成绩
score=[
    {'name':'A','score':98},
    {'name':'B','score':86},
    {'name':'C','score':95},
    {'name':'D','score':100}
]
score.sort(key=lambda x:x['score'],reverse=True)#***key是关键***
print(score)