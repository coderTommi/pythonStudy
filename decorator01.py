def pre_str(pre=''):
    def decorator(F):
        def new_F(a,b):
            print (pre+'input: ',a,b)
            return F(a,b)
        return new_F
    return decorator
#@decorator
@pre_str('^_^')
def ssum(a,b):
    return a**2+b**2

#@decorator
@pre_str('T_T')
def sdiff(a,b):
    return a**2-b**2

ssum(3,4)
sdiff(5,6)

#newsum=decorator(ssum)
#newsum(8,9)
