"""
#类的组成：
 1.类属性：直接定义在类中，方法外的变量
 2.实例属性：定义在_init_方法中，使用self打点的变量
 3.实例方法：定义在类中的函数，而且自带参数self
 4.静态方法：使用装饰器@staticmethod修饰的方法
 5.类方法：使用装饰器@classmethod修饰的方法

class 类名():
   pass
对象名=类名()
"""

class Person:#括号可以省略不写
    pass
class Cat:
    pass
per=Person()
cat=Cat()
print(type(Person))
print(type(per))
print(type(cat))

class Student:
    school='NJU'#类属性
    def __init__(self,name,age):#name,age是方法的参数，是局部变量，作用域为整个_init_方法
        self.name=name#将局部变量的值赋值给实例属性
        self.age=age#实例属性和局部变量名字可以相同
    def show(self):
        print('姓名：',self.name,'年龄：', self.age)
    @staticmethod
    def sm():
        #print(self.name)
        #self.show()
        print('这是一个静态方法，不能调用实例属性，不能调用实例方法')
    @classmethod
    def my(cls):#cls是class的简写
        #print(self.name)
        #self.show()
        print('只是一个类方法，不能调用实例属性，不能调用实例方法')

stu=Student('fyz','20')
print(Student.school)
print(stu.name,stu.age)
stu.show()
Student.sm()
Student.my()
stu.sm()
stu.my()

#创建多个对象
stu1=Student('1',18)
stu2=Student('2',20)
stu3=Student('3',21)
stu4=Student('4',15)
lst=[stu1,stu2,stu3,stu4]
for i in lst:
    i.show()
