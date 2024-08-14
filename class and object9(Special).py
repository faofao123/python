"""
特殊方法（没有用）
特殊属性
obj.__dict__   对象的属性字典
obj.__class__  对象所属的类
class.__bases__类的父亲元组
class.__base__ 类的父类
class.__mro__  类的层次结构
class.__subclasses__()类的子类列表

"""
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
a=A()
b=B()
c=C('fyz',20)
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)

print(a.__class__)
print(b.__class__)
print(c.__class__)

print(A.__bases__)
print(B.__bases__)
print(C.__bases__)

print(A.__base__)
print(B.__base__)
print(C.__base__)#显示第一个父类

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)#层次结构==族谱

print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())