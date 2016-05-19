class num(object):
    def __init__(self,value):
        self.value=value
    def getNeg(self):
        return -self.value
    def setNeg(self,value):
        self.value=-value
    def delNeg(self):
        print("value is deling")
	del self.value
    neg=property(getNeg,setNeg,delNeg,"I'm the doc")
 
n=num(5)
print n.value
n.neg=10
print n.value
print num.neg.__doc__
del n.neg
