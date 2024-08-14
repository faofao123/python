"""
#json模块常用函数
1.json.dumps(obj)       将Python数据类型转成JSON格式过程，编码过程
2.json.loads(s)         将JSON格式字符串转成Python数据类型，解码过程
3.json.dump(obj,file)   与dumps()功能相同，将转换结果存储到文件file中
4.json.load(file)       与loads()功能相同，从文件file中读入数据
"""
import json
lst=[{'name':'fyz','age':20,'score':100},
     {'name':'ss','age':20,'score':99},
     {'name':'哈哈哈','age':20,'score':98}
     ]
s=json.dumps(lst,ensure_ascii=False,indent=4)#ensure_ascii正常显示中文，indent增加数据的缩进。
print(type(s),s)

lst2=json.loads(s)
print(type(lst2),lst2)

with open('./attachments/f.txt','w',encoding='utf-8') as f:
    json.dump(lst,f,ensure_ascii=False,indent=4)

with open('./attachments/f.txt','r',encoding='utf-8') as f:
    lst3=json.load(f)
    print(type(lst3),lst3)