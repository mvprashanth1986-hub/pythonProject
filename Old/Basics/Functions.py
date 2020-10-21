def test():
    print("whooo lalala")

test()

def test1(a):
    print(a+5)

test1(100)

def name(str1="India"):
    print(str1)

name("USA")

def country_names(x):
    for i in x:
        print(i)

x = ["India","US","UK","NY"]
country_names(x)

def rec(num):
    if (num>1):
        num = num*rec(num-1)
    return num

fact = rec(3)
print(fact)

def login(username,password):
    print("login with %s and %s" %(username, password))

login("pra@gmail.com","pass@1")