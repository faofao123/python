"""
*time模块
1.time()             获取当前时间戳
2.localtime(sec)     获取指定时间戳对应的本地时间的struct_time对象
3.ctime()            获取当前时间戳对应的易读字符串
4.strftime()         格式化时间，结果为字符串
5.strptime()         提取字符串的时间，结果为struct_time对象
6.sleep(sec)         休眠sec秒
———————————————————————————————————————————
*格式化字符串
%Y 年份
%m 月份
%B 月名
%d 日期
%A 星期
%H 小时（24小时制）
%I 小时（12小时制）
%M 分钟
%S 秒
"""
import time
now=time.time()
print(now)

obj=time.localtime(now)
print(obj)
print(obj.tm_year)
print(obj.tm_wday)      #[0,6]

print(time.ctime())     #Sat Aug 10 18:51:46 2024
#time转换成字符串
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#字符串转换成time时间
print(time.strptime('2008-08-08', '%Y-%m-%d'))

time.sleep(5)
print('hello')