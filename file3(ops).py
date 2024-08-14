def my_read(filename):
    file= open(filename,'w+',encoding='utf-8')
    file.write('你好啊\n你是谁')#此时指针在'谁'的后面
    #seek修改文件指针的位置
    file.seek(0)#使指针回到文件起始位置  可以调整参数的值，后移x个字节
    #读取
    s=file.read()
    print(type(s),s)
    file.close()

def my_readsize(filename):
    file= open(filename,'r',encoding='utf-8')
    s=file.read(2)#2个字符
    print(type(s),s)
    file.close()

def my_readline(filename):
    file= open(filename,'r',encoding='utf-8')
    s=file.readline()#读取一行
    print(type(s),s)
    file.close()
def my_readlinesize(filename):
    file= open(filename,'r',encoding='utf-8')
    s=file.readline(2)#读取一行2个字符
    print(type(s),s)
    file.close()

def my_readlines(filename):
    file= open(filename,'r',encoding='utf-8')
    s=file.readlines()#读取所有，一行为列表中的一个元素，s是列表类型
    print(type(s),s)
    file.close()
if __name__ == '__main__':
    my_read('attachments/c.txt')
    my_readsize('attachments/c.txt')
    my_readline('attachments/c.txt')
    my_readlinesize('attachments/c.txt')
    my_readlines('attachments/c.txt')