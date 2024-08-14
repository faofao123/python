#根据变量所引用的数据类型，动态决定调用哪个对象中的方法
#python中不关心数据类型、不关心是否继承、只关心对象的行为（方法）。
#只要不同的类中有同名的方法，就可以实现多态
class Person:
    def eat(self):
        print('fruit')
class Cat:
    def eat(self):
        print('fish')
class Dog:
    def eat(self):
        print('meat')

def fun(obj):
    obj.eat()
per=Person()
cat=Cat()
dog=Dog()
fun(per)
fun(cat)
fun(dog)