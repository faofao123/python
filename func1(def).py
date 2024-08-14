"""
#函数的定义与调用
def 函数名称(参数列表):
   函数体
   [return 返回值列表]

"""
def getsum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    print(s)
getsum(100)

#函数的参数传递（23不重要，记住1就行）
#1.位置参数
#2.关键字参数
#3.默认值参数
def happybirthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

happybirthday('fyz',20)#1

happybirthday(age=20,name='fyz')#2

def happybirthday(name='fyz',age=20):#3
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')
happybirthday()#不传参函数用默认参数
happybirthday('fyz')
happybirthday(age=21)
happybirthday('fyz',20)

#————————————————————————————————————————————————————
#可变参数（）
#1.个数可变的位置参数    *para
#2.个数可变的关键字参数  **para
def fun(*para):
    print(type(para))
    for item in para:
        print(item)
fun(1,2,3,4)
fun([1,2,3,4])
fun(*[1,2,3,4])#参数前加*，对列表进行解包

def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,value)
fun2(a=1,b=2,c=3)
d={'a':1,'b':2,'c':3}
fun2(**d)#参数前加**，对字典解包