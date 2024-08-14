"""
 数据的组织维度：也称为数据的组织方式或存储方式，在Python中常用的数据组织方式可分为一维数据、二维数据和高维数据。
 1.一维数据
 通常采用线性方式组织数据，一般使用Python中的列表、元组或者集合进行存储数据。
 2.二维数据
 二维数据也称表格数据，由行和列组成，类似于Excel表格，在Python中使用二维列表进行存储。
 3.高维数据
 高级数据则是使用Key-Value方式进行组织数据，在Python中使用字典进行存储数据。在Python中内置的json模块专门用于处理JSON(JavaScript Object Notation)格式的数据。

"""
def my_write():
    lst=['a','b','c']
    with open('./attachments/e.txt','w') as f:
        f.write(','.join(lst))#列表转成字符串才能写进去
        f.write('\n')

def my_read():
    with open('./attachments/e.txt','r') as f:
        s=f.read()
        lst=s.split(',')     #字符串转换成列表
        print(lst)

def my_write_table():
    lst=[
        ['商品名称','单价','采购数量'],
        ['水杯','98.5','20'],
        ['鼠标','89','100']
    ]
    with open('./attachments/e.txt','a',encoding='utf-8') as f:
        for item in lst:
            f.write(','.join(item))
            f.write('\n')

def my_read_table():
    data=[]                 #初始化二维列表
    with open('./attachments/e.txt','r',encoding='utf-8') as f:
        lst=f.readlines()   #每一行是列表中的一个元素
        for line in lst:
            new_lst=line[:len(line)-1].split(',')
            data.append(new_lst)
    print(data)

if __name__ == '__main__':
    my_write()
    my_read()
    my_write_table()
    my_read_table()