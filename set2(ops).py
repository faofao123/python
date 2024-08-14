#集合的操作符
#1.交并补差
#2.增删改
A={1,2,3,4,5}
B={4,5,6,7,8}

#交集操作
print(A&B)
#并集操作
print(A|B)
#补集操作(A|B-A&B)
print(A^B)
#差集操作
print(A-B)
print(B-A)

"""
s.add(x)如果x不在集合中，则将x添加到集合s
s.remove(x)如果x在集合中，删除；不在，程序报错
s.clear()清除集合所有元素
"""
A.add(10)
print(A)
A.remove(10)
print(A)
#A.remove(10)   KeyError: 10
A.clear()
print(A)#空集合

#集合遍历
for item in B:
    print(item,end=' ')
print()
for index,item in enumerate(B):
    print(index,':',item,end='      ')
print()

#集合生成式
s={i for i in range(10)}
print(s)
s={i for i in range(10) if i%2==0}
print(s)
