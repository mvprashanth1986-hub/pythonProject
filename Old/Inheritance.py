class Test:

    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

    def isemployee(self):
        return True

class child(Test):
    def isemployee(self):
        return False

e1 = Test("James")
print(e1.getname())
print(e1.isemployee())

e2 = child("Bond")
print(e2.getname())
print(e2.isemployee())

print(issubclass(Test,child))