"""
1.文件的打开模式
r   以只读模式打开，文件指针在文件的开头，如果文件不存在，程序抛异常
rb  以只读模式打开二进制文件，如图片文件
w   覆盖写模式，文件不存在创建，文件存在则内容覆盖
wb  覆盖写模式写入二进制数据，文件不存在则创建，文件存在则覆盖
a   追加写模式，文件不存在创建，文件存在，则在文件[最后]追加内容
+   与w/r/a等一同使用，在原功能的基础上增加同时读写功能

2.文件的基本操作
 file.read(size)
 从文件中读取size个字符或字节，如果没有给定参数，则读取文件中的全部内容
 file.readline(size)
 读取文件中的一行数据，如果给定参数，则为读取这一行中的size个字符或字节
 file.readlines()
 从文件中读取所有内容，结果为列表类型
 file.write(s)
 将字符串s写入文件
 file.writelines(lst)
 将内容全部为字符串的列表lst写入文件
 file.seek(offset)
 改变当前文件操作指针的位置，英文占一个字节，中文gbk编码占两个字节，utf-8
 编码占三个字节

"""
def my_write(s):
    file=open('attachments/b.txt', 'a', encoding='utf-8')
    file.write(s)
    file.write('\n')
    file.close()

def my_write_list(file,lst):
    f=open(file,'a',encoding='utf-8')
    f.writelines(lst)
    f.close()

#每执行一次都会在末尾追加一次
# my_write('hello')
# my_write('world')
# my_write_list('b.txt',['hello','world'])