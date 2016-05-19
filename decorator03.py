#coding:utf-8
def juedui(x):
    return abs(x)
def kaifang(F):
    def newF(x):
        return F(x)**0.5
    return newF

def xiangfan(F):
    def newF(x):
        return -F(x)
    return newF

func=xiangfan(kaifang(juedui))
print func(49)
