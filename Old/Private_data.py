class Employee:
    __salary = 1000     #private variable

e1 = Employee()
print(e1._Employee__salary)     #trick to access private hiden variable

class Test:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "a:%s  b:%s" %(self.x,self.y)

    def __str__(self):
        return "value of a is %s and b is %s" %(self.x,self.y)

t = Test(1,2)
print(t)