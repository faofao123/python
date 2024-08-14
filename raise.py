#python中的异常处理
#raise [Exception类型（异常描述信息）]
try:
    gender=input('请输入您的性别：')
    if gender !='男' and gender !='女':
        raise Exception('性别只能是男或女')
    else:
        print(gender)
except Exception as e:
    print(e)