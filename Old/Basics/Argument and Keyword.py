#Different ways of passing argument
def login(username,password):
    print(username,password)

login("mvprashanth1986@gmail.com","password@1")
login(username="mvprashanth1986@gmail.com",password="password@1")

def marks(*arg):
    for x in arg:
        print(x)

marks(10,20,30,40)
marks("abc","xyz","bamboo","jasmine")

def marks1(*arg):
    for x in range(len(arg)):
        print(arg[x])
        print(arg[2])

marks1(10, 20, 30, 40)
marks1("abc", "xyz", "bamboo", "jasmine")

#Passing argument keys
def make(**arg):
    for key,value in arg.items():
        print("%s = %s"%(key,value))

make(autom=9,manual=9,api=9)

ele = lambda x: x*x*x
print (ele(5))


