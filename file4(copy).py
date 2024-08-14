def copy(src,new_path):
    #文件的复制就是读写操作
    file1=open(src,'rb')
    file2=open(new_path,'wb')
    s=file1.read()
    file2.write(s)
    file2.close()
    file1.close()#先打开的后关，后打开的先关

if __name__=='__main__':
    src= './attachments/艾丽妮.png'  #.代表的是当前目录(..表示的是上级目录)
    new_path='./attachments/new_att/copy_艾丽妮.png'
    copy(src,new_path)