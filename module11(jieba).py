#jieba是用于对中文进行分词的模块，它可以将一段中文文本分割成中文词组的序列
import jieba
#读取文件
with open('./!!!使用说明.txt','r',encoding='utf-8') as file:
    text = file.read()
# print(text)
#分词
lst=jieba.lcut(text)
# print(lst)

#去重操作
set1=set(lst)

d={}#key:词,value:出现的次数
for item in set1:
    if len(item)>1:
        d[item]=0
#print(d)
#统计次数
for item in lst:
    if item in d:
        d[item]+=1
new_lst=[]
for item in d:
    new_lst.append([item,d[item]])
# print(new_lst)

#列表排序
new_lst.sort(key=lambda x: x[1], reverse=True)
print(new_lst[0:11])