#动态绑定属性和方法
class Student:
    school='NJU'
    def __init__(self,name,age):#name,age是方法的参数，是局部变量，作用域为整个_init_方法
        self.name=name#将局部变量的值赋值给实例属性
        self.age=age#实例属性和局部变量名字可以相同
    def show(self):
        print('姓名：',self.name,'年龄：', self.age)

stu1=Student('fyz',20)
stu2=Student('zjn',20)

#为stu2动态创建一个属性
stu2.gender='女'
print(stu2.gender)
#动态绑定方法
def introduce():
    print('zjn的一个动态方法')
stu2.fun=introduce
stu2.fun()