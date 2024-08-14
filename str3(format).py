"""
格式化字符串
1.占位符 %s字符串   %d十进制整数    %f浮点数(%.nf 保留n位小数)
2.f-string
3.str.format()  |以及其他用法

"""
name='fyz'
age=18
score=98.5
print('姓名:%s,年龄:%d,成绩:%.2f' %(name,age,score))

print(f'姓名:{name},年龄:{age},成绩:{score}')

print('姓名:{0},年龄:{1},成绩:{2}'.format(name,age,score))

#千位分隔符（适用于整数和浮点数）
print('{0:,}'.format(987654321))
#浮点数精度
print('{0:.2f}'.format(3.1415926))
#二进制
print('{0:b}'.format(4))
#科学计数法
print('{0:.2e}'.format(3.1415926))
#百分数
print('{0:%}'.format(3.1415926))
