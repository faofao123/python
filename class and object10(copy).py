"""
#类的深拷贝与浅拷贝
1.变量的赋值：只是形成两个变量，实际上指向同一个对象
2.浅拷贝：拷贝时，对象包含的子对象内容不拷贝，因此源对象与拷贝对象会引用同一个子对象
3.深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同

"""
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu=CPU()
disk=Disk()
com=Computer(cpu,disk)
#1
com1=com
print(com,com.cpu,com.disk)
print(com1,com1.cpu,com1.disk)#内存地址相同
print()
#2
import copy
com2=copy.copy(com)
print(com,com.cpu,com.disk)
print(com2,com2.cpu,com2.disk)#子对象内存地址一样
print()
#3
com3=copy.deepcopy(com)
print(com,com.cpu,com.disk)
print(com3,com3.cpu,com3.disk)#完全建立了一个新的对象