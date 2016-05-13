#-*- coding:utf-8 -*-
def writeFile(file='record.txt'):
    f=open(file,'a+')
    f.write('tom, 12, 86\n')
    f.write('Lee, 15, 99\n')
    f.write('Lucy,11, 58\n')
    f.write('Josepy, 19 , 56\n')
    f.close()
    f=open('record.txt','r')
    print f.readlines()

writeFile()
