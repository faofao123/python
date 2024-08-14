#函数的返回值
def calc(a,b):
    return a+b
print(calc(1,2))

#返回值是多个，返回值类型为元组类型
def getsum(n):
    s=0
    ji=0
    ou=0
    for i in range(n):
        s+=i
        if i%2==0:
            ou+=i
        else :
            ji+=i
    return s,ji,ou
print(getsum(100))
a,b,c=getsum(100)#***解包元组***
print(a,b,c)