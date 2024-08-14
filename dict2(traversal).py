"""
取值  d[key]  d.get(key)
遍历字典
1. for element in d.items():
      pass
2. for key,value in d.items():
      pass

"""
d={'hello':1,'world':2}
print(d['hello'])
print(d.get('hello'))
#区别：若键不存在，d.[]会报错；d.get()不会报错，会返回默认值(none)，默认值可以手动改变
# print(d['python'])
print(d.get('python'))
print(d.get('python','不存在'))

for item in d.items():
    print(item)#输出是元组模式

for key,value in d.items():
    print(key,value)
