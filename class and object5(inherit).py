"""
#继承
1.一个子类可以继承多个父类
2.一个父类可以拥有多个子类
3.如果一个类没有继承任何类，默认继承object类

class 类名(父类1，父类2……，父类N):
    pass

"""
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, sno):
#—————————————————————————————————————————————————————————
        super().__init__(name, age)     #调用父类的初始化方法
#—————————————————————————————————————————————————————————
        self.sno = sno

class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

stu1=Student('fyz',20,'221900402')
stu1.show()
stu2=Doctor('fyz',20,'临床')
stu2.show()

#-------------------------------------------------------
#多继承
class FatherA:
    def __init__(self,name):
        self.name = name
    def showA(self):
        print('A')

class FatherB:
    def __init__(self,age):
        self.age = age
    def showB(self):
        print('B')

class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
#————————————————————————————————————————————————————
        FatherA.__init__(self,name)#调用不同父亲的方法
        FatherB.__init__(self,age)
#————————————————————————————————————————————————————
        self.gender = gender
    def show(self):
        print(self.name,self.age,self.gender)

son=Son('fyz',20,'男')
son.showA()
son.showB()
son.show()