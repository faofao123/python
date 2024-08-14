"""
文件的基本操作
1.打开文件：变量名=open(filename,mode,encoding) #如果文件不存在，则新建
2.操作文件: 变量名.read()
           变量名.write(s)
3.关闭文件: 变量名.close()
"""
def my_write():
    file=open('attachments/a.txt', 'w', encoding='utf-8')
    file.write('fyz')
    file.close()
my_write()

def my_read():
    file=open('attachments/a.txt', 'r', encoding='utf-8')
    s=file.read()
    file.close()
    return s

str=my_read()
print(str)