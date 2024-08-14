"""
字符串常用操作
str.relpace(old,news)使用news替换字符串s中所有的old字符串，结果是一个新的字符串
str.center(width,fillchar)字符串str在指定的宽度范围内居中，可以使用fillchar进行填充
str.join(iter)在iter中的每一个元素的后面都增加一个新的字符串str
str.strip(chars)从字符串中去掉左侧和右侧chars中列出的字符串
str.lstrip(chars)从字符串中去掉左侧chars中列出的字符串
str.rstrip(chars)从字符串中去掉右侧chars中列出的字符串

"""
s1='HelloWorld'
news1=s1.replace('o','你好')
print(news1)
news1=s1.replace('o','你好',1)#count为替换次数
print(news1)

print(s1.center(20,'*'))

s2='   hello world   '
print(s2.strip())#去除空格
print(s2.rstrip())
print(s2.lstrip())

s3='dl-helloworld'
print(s3.strip('ld'))#与顺序无关
print(s3.strip('dl'))
