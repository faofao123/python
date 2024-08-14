"""
***requests***爬虫！

1.是用于处理HTTP(Hypertext Transfer Protocol超文本传输协议)请求的第三方库，该库在爬虫程序中应用非常广泛。
2.使用requests库中的get()函数可以打开一个网络请求，并获取一个Response响应对象。
3.响应结果中的字符串数据可以通过响应对象的text属性获取
4.响应结果中除了有字符串数据也有二进制数据，响应结果中的二进制数据可以通过响应对象的content属性获取

"""
import requests
import re
url='http://www.weather.com.cn/weather1d/101010100.shtml'
resp=requests.get(url)
#设置编码格式(中文)
resp.encoding='utf-8'
# print(resp.text)

city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
print(city)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
print(weather)
wd=re.findall('<span class="wd">(.*)</span>',resp.text)
print(wd)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)
print(zs)

#数据打包
lst=[]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d])
for i in lst:
    print(i)
"""
['景区', '天气', '气温', '旅游指数']
['三亚', '多云', '27/34℃', '适宜']
['九寨沟', '晴', '17/31℃', '适宜']
['大理', '中雨转小雨', '17/24℃', '一般']
['张家界', '多云', '25/37℃', '适宜']
['桂林', '阵雨', '27/33℃', '适宜']
['青岛', '阴转晴', '28/32℃', '适宜']
"""
#爬取图片并保存到本地
new_url='https://search-operate.cdn.bcebos.com/e8cbce1d53432a6950071bf26b640e2b.gif'
resp=requests.get(new_url)
with open('./attachments/logo.gif', 'wb') as file:
    file.write(resp.content)


'''
    【zip()函数】
zip对象产生n个长度的元组，每个元组中的第i个元素
来自zip()的第i个可迭代参数。这种情况一直持续到
最短的论点已经穷尽。
'''
