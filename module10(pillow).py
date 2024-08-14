#PIL是用于图像处理的第三方库，它支持图像存储、处理和显示等操作
from PIL import Image

#——————实现图像颜色的交换——————#
#加载图片
im=Image.open('./attachments/艾丽妮.png')
# print(type(im),im)

#提取RGB图像的颜色通道，返回结果是图像的副本
r,g,b=im.split()
#合并通道
om=Image.merge(mode='RGB',bands=[r,b,g])
om.save('./attachments/new_att/新艾丽妮.png')