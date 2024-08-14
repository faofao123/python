#字符串的拼接与去重
s1='hello'
s2='world'

#'+'拼接
print(s1+s2)

#字符串的join函数(括号里是列表)
print(''.join([s1,s2]))
print('*'.join(['hello','world','python']))

#直接拼接
print('hello''world')

#格式化字符串拼接
print('%s%s'%(s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))

#去重操作——————————————————————————————————————————————————————
#1.通过循环
s='dasdfasdafasdcsvcsfd'
news=''
for i in s:
    if i not in news:
        news+=i
print(news)
#2.通过集合
news2=set(s)
print(news2)
lst=list(news2)
print(lst)
lst.sort(key=s.index)#根据在原字符串中的位置排序
print(''.join(lst))
