"""
 os.path模块：是os模块的子模块，也提供了一些目录或文件的操作函数。

 1.abspath(path)
 获取目录或文件的绝对路径
 2.exists(path)
 判断目录或文件在磁盘上是否存在，结果为bool类型，如果目录或文件
 在磁盘上存在，结果为True,否则为False
 3.join(path,name)
 将目录与目录名或文件名进行拼接，相当于字符串的“+”操作
 4.splitext()
 分别获取文件名和后缀名
 5.basename(path)
 从path中提取文件名
 6.dirname(path)
 从path中提取路径(不包含文件名)
 7.isdir(path)
 判断path是否是有效路径
 8.isfile(path)
 判断file是否是有效文件

"""
import os

print('绝对路径：',os.path.abspath('./attachments/a.txt'))
print('判断文件是否存在:',os.path.exists('./attachments/a.txt'))
print('判断目录是否存在：',os.path.exists('./attachments'))
print('拼接路径：',os.path.join('./attachments','a.txt'))
print('文件的名和文件后缀名：',os.path.splitext('b.txt'))
print('提取文件名：',os.path.basename('./attachments/a.txt'))
print('提取路径：',os.path.dirname('./attachments/a.txt'))
print('判断是否是有效路径',os.path.isdir('./attachment'))            #少个s
print('判断文件是否有效：',os.path.isfile('./attachments/aa.txt'))   #多个a