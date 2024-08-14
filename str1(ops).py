"""
字符串是不可变数据类型
字符串常用操作
str.lower()将字符串全部转换成小写，结果为一个新的字符串
str.upper()将字符串全部转换成大写，结果为一个新的字符串
str.split(sep=None)把字符串按照指定的分隔符sep进行分隔，结果为列表类型
str.count(sub)结果为sub这个字符串在str中出现的次数
str.find(sub)查询sub在str中是否出现，如果不出现结果为-1;如果存在，结果为sub首次出现的索引
str.index(sub)功能与find相同，区别在于要查询的sub不存在时报错
str.startswith(s)查询字符串str是否以子串s开头
str.endswith(s)查询字符串str是否以子串s结尾

"""
s1='Hello World'
print(s1)
news1=s1.upper()
print(news1)

e_mail='fyz@163.com'
s2=e_mail.split('@')
print(s2)

print(s1.count('o'))
print(s1.find('o'))
print(s1.find('p'))  #-1
print(s1.index('o'))
# print(s1.index('p')) ValueError: substring not found

print('demo.py'.endswith('.py'))
print('text.txt'.endswith('.py'))
print(s1.startswith('H'))
print(s1.startswith('p'))