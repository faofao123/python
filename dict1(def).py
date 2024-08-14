"""
#字典类型是根据一个信息查找另一个信息的方式构成了‘键值对’,可变序列
创建方式
1. d={key1:value1,key2:value2……}
2. dict(key1=value1,key2=value2……)关键字参数的键必须是字符串类型
3. zip(list1,list2)

"""
d={1:'cat',2:'dog',1:'pet'}#有重复键值会覆盖之前的
print(d)

lst1=[1,2,3]
lst2=['cat','dog','pet']
obj=zip(lst1,lst2)
print(zip(lst1,lst2))
# print(list(obj))#将zip类型转换成列表类型
d1=dict(obj)#将zip类型转换成字典类型
print(d1)

d2=dict(cat=1,dog=2,pet=3)
print(d2)

t=(1,2,3)
print({t:10})#元组可以作为键值

# list=[1,2,3]
# print({list:10})错误，可变序列不可作为键值

print(max(d1))
print(max(d2))
print(len(d))

del d
