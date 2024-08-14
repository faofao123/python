"""
字典生成式
1. d={key:value for item in range}
2. d={key:value for key,value in zip(lst1,lst2)}

"""
import random
d={item:random.randint(1,100) for item in range(1,11)}
print(d)

lst1=[1,2,3,4]
lst2=['a','b','c','d','e','f','g','h']#两个列表数量不相同时，以少的那个建立字典个数
obj=zip(lst1,lst2)
d={key:value for key,value in obj}
print(d)
