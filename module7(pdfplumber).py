#pdfplumber可用于从PDF文件中读取内容
import pdfplumber
#打开文件
with pdfplumber.open("./attachments/卷积神经网络研究综述.pdf") as pdf:
    pages = pdf.pages               #页数
    for page in pages:
        print(page.extract_text())  #extract_text()提取内容
        print(f'-------第{page.page_number}页结束')
