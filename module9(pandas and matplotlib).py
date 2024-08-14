"""
 Pandas 与 Matplotlib
 1.Pandas是基于 Numpy模块扩展的一个非常重要的数据分析模块，
    使用 Pandas读取 Excel数据更加的方便
 2.Matplotlib是用于数据可视化的模块，
    使用 Matplotlib.pyplot可以非常方便的绘制饼图、柱形图、折线图等。
"""
import pandas as pd
import matplotlib.pyplot as plt

#读取Excel文件
df=pd.read_excel('./attachments/老师打分表.xlsx')
# print(df)
#解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
#设置画布的大小
plt.figure(figsize=(10,6))
labels=df['姓名']
y=df['汇总']
# print(labels)
# print(y)

#绘制饼图
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90)
#设置x，y轴刻度
plt.axis('equal')
plt.title('老师分数占比图')
plt.show()