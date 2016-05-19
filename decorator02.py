def decorator(aClass):
    class newClass:
        def __init__(self,age):
	    self.total_display=0
	    self.wrapped=aClass(age)
	def display(self):
	    self.total_display +=1
	    print ("total display", self.total_display)
	    self.wrapped.display()
    return newClass

@decorator
class bird:
    def __init__(self,age):
        self.age=age
    def display(self):
        print("My age is ", self.age)

bbb=bird(5)
for i in range(5):
    bbb.display()
