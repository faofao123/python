"""
#权限控制
1.单下划线：protected 允许类本身和子类访问，但实际上可以被外部代码访问
2.双下划线：private   只允许类本身访问
3.首尾双下划线：一般表示特殊的方法

"""

class Student:
    def __init__(self, name, age,gender):
        self._name = name
        self.__age = age#只允许类本身访问
        self.gender = gender

    def _fun(self):
        print('protected')
    def __fun2(self):
        print('private')
    def show(self):
        self._fun()
        self.__fun2()
        print(self._name)
        print(self.__age)

stu=Student('fyz',20,'男')
print(stu._name)
# print(stu.__age)  AttributeError: 'Student' object has no attribute '__age'.
stu._fun()
# stu.__fun2()  AttributeError: 'Student' object has no attribute '__fun2'.

#私有属性和方法的访问(非常不推荐)
print(stu._Student__age)
stu._Student__fun2()
print(dir(stu))
# ['_Student__age', '_Student__fun2', '__class__', '__delattr__',
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getstate__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__le__',
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', '_fun', '_name',
# 'gender', 'show']