"""
#with语句
    又称为上下文管理器，在处理文件时，无论是否产生异常，都能保证with语句执行完毕后关闭已经打开的文件
这个过程是自动的，无需手动操作。
语法结构：
with open(……) as file:
    pass

"""
def write_fun():
    with open('attachments/d.txt', 'w', encoding='utf-8') as file:
        file.write('2024/8/13')

def read_fun():
    with open('attachments/d.txt', 'r', encoding='utf-8') as file:
        print(file.read())

def copy_fun(src_file,target_file):
    with open(src_file,'r',encoding='utf-8') as file1:
        with open(target_file,'w',encoding='utf-8') as file2:
            file2.write(file1.read())

if __name__ == '__main__':
    write_fun()
    read_fun()
    copy_fun('attachments/d.txt', './attachments/new_att/d.txt')
