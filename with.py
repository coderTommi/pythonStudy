#coding:utf-8
with open('new.txt','w') as f:
    print f.closed
    f.write('helloworld')
print f.closed
