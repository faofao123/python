#Numpy用于处理数组、矩阵等数据
import numpy as np
import matplotlib.pyplot as plt

#读取图片
n1=plt.imread('./attachments/艾丽妮.png')
print(n1,type(n1))   #<class 'numpy.ndarray'>  三维数组：最高维度表示图像的高，次高维度表示图像的宽，最低维[R,G,B]颜色
plt.imshow(n1)

#灰度公式
n2=np.array([0.299,0.587,0.114])
#将n1(RGB)颜色值与数组n2(灰度公式固定值)进行矩阵运算
x=np.dot(n1,n2)
#传入数组，显示灰度
plt.imshow(x,cmap='gray')
#显示图像
plt.show()

