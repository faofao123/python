"""
——————OS目录与文件的相关操作
 Python内置的与操作系统文件相关的模块，该模块中语句的执行结果通常与操作系统有关，即有些函数的运行效果在Windows操作系统和MacOS系统中不一样。
——————函数
 1.getcwd()         获取当前的工作路径
 2.listdir(path)    获取path路径下的文件和目录信息，如果没有指定path,则获取当前路径下的文件和目录信息
 3.mkdir(path)      在指定路径下创建目录(文件夹)
 4.makedirs(path)   创建多级目录
 5.rmdir(path)      删除path下的空目录
 6.removedirs(path) 删除多级目录
 7.chdir(path)      把path设置为当前目录
 8.walk(path)       遍历目录树，结果为元组，包含所有路径名、所有目录列表和文件列表
 9.remove(path)     删除path指定的文件
 10.rename(old,new) 将old重命名为new
 11.stat(path)      获取path指定的文件信息
 12.startfile(path) 启动path指定的文件

"""
import os
print(os.getcwd())
lst1=os.listdir()
print(lst1)
# lst2=os.listdir('D:/jetbrians/PycharmProjects')
# print(lst2)

#os.mkdir('./好好学习')        当该目录已存在时，报错
#os.makedirs('./aa/bb/cc')    多级目录
#os.rmdir('./好好学习')         删除的目录不为空或者不存在，都会报错
#os.removedirs('./aa/bb/cc')    所涉及的目录都删除

# os.chdir('D:/jetbrians/PycharmProjects')
# print(os.getcwd())

# for dirs,dirlst,filelst in os.walk('D:/jetbrians/PycharmProjects'):
#     print(dirs)     #路径名
#     print(dirlst)   #目录列表
#     print(filelst)  #文件列表
#     print('------------------------')

#os.remove('./a.txt')   若文件不存在，报错
#os.rename('./a.txt','./b.txt')

import time
def date_format(longtime):
    s=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))
    return s

info=os.stat('./attachments/a.txt')
print(type(info),info)

print('最近的一次访问时间：',date_format(info.st_atime))
print('文件的创建时间：',date_format(info.st_ctime))
print('文件的大小(单位是字节)：',info.st_size)

os.startfile('calc.exe')
# os.startfile(r"D:\Program Files (x86)\Wuthering Waves\launcher.exe")     鸣潮启动！

#[拓展]
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))上级文件地址
#BASE_DIR=os.path.dirname(os.path.realpath(sys.argv[0])) 上级文件地址
