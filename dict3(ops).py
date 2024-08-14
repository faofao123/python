"""
字典相关操作
d.keys()           获取所有key数据
d.values()         获取所有value数据
d.pop(key,default)若key存在，获取相对应的value，同时删除key-value对;否则获取默认值
d.popitem()       随即从字典中取出一个key-value对，结果为元组类型，且将该对从字典中删除
d.clear()         清空字典所有key-value对

"""
d={1001:'李梅',1002:'王华',1003:'张锋'}
print(d)

d[1004]='张丽丽'#添加元素
print(d)

keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

values=d.values()
print(values)
print(list(values))
print(tuple(values))

lst=list(d.items())#键值对
print(lst)

d1=dict(lst)
print(d1)

print(d.pop(1001))
print(d)

print(d.pop(1008,'NULL'))
print(d)

print(d.popitem())
print(d)

d.clear()
print(d)