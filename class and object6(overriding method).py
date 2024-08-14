#父亲的方法并不能完全适合子类的需求，这个时候就可以重写父类的方法
#在重写父类方法时，要求方法的名称必须与父类的名称相同，在子类重写后的方法中可以用super().xxx()调用父类中的方法
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, sno):
        super().__init__(name, age)
        self.sno = sno

    def show(self):
        super().show()
        print(self.sno)

class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    def show(self):
        print(self.department)

stu1=Student('fyz',20,'221900402')
stu2=Doctor('fyz',20,'临床')
stu1.show()
stu2.show()