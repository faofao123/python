"""
集合无序的【不重复】序列，集合中只能存放不可变数据类型
集合本身是可变数据类型
#创建方式
1. s={element1,element2,……,elementN}
2. s=set(可迭代对象)
删除 del 集合名

"""
s={1,2,3,4}
print(s,type(s))

# s={[1,2],[3,4]}  TypeError: unhashable type: 'list'

s=set()#创建空集合
print(s)

s={}#字典
print(s,type(s))

s=set('helloworld')
print(s)

s=set([1,2,3,4])
print(s)

s=set(range(1,11))
print(s)

print(max(s))
print(min(s))
print(sum(s))
print(len(s))
print(9 in s)

del s
