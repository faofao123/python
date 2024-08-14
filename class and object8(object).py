"""
#object类
所有类直接或间接的父类
所有类拥有object类的属性和方法
__new__()有系统调用，用于创建对象
__init__()手动调用，用于初始化对象属性值
__str__()对象的描述，返回值是str类型，默认输出对象的内存地址

"""
class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)
    def __str__(self):      #***重写父类方法***
        return f'{self.name} is {self.age}'

per=Person('fyz',20)
print(dir(per))
print(per)