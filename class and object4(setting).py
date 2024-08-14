#属性的设置
class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    @property         #***将方法转换成属性使用***
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender):
        if gender !='男' and gender !='女':
            print('输入错误，已设计成默认男')
            self.__gender='男'
        else:
            self.__gender = gender
stu=Student('Jack','男')
print(stu.name, stu.gender)#stu.gender就会去执行stu.gender()

# stu.gender = 'Male'   #AttributeError: property 'gender' of 'Student' object has no setter
stu.gender='女'
print(stu.name, stu.gender)
stu.gender='qita'
print(stu.name, stu.gender)