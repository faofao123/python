"""
python 3.11新特性
1.结构模式匹配
match data:
  case{}:
      pass
  case[]:
      pass
  case():
      pass
  case_:
      pass
2.字典合并运算符|
3.同步迭代
match data1,data2:
  case data1,data2:
      pass

data=eval(input('请输入：'))
match data:
    case {'name':'fyz','age':20}:
        print('字典')
    case [1,2,3]:
        print('列表')
    case (1,2,3):
        print('元组')
    case _:
        print('else')

"""

d1={'a':1,'b':2,'c':3}
d2={'d':1,'e':2,'f':3}
print(d1|d2)

fruits={'apple','banana','cherry'}
counts=[10,3,4]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'banana',3:
            print('3个香蕉')
        case 'cherry',4:
            print('4个樱桃')
#输出结果会变化，因为fruits是集合，是无序的
