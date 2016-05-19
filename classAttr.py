class bird(object):
    feature=True

class chicken(bird):
    fly=False
    def __init__(self,age):
        self.age=age

summer=chicken(2)
print(bird.__dict__)
print(chicken.__dict__)
print(summer.__dict__)
print chicken.__base__
