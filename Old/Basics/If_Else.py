a = 100
b = 2001
c = 300
if a>b and a>c:
    print("a is highest")
elif b>a and b>c:
    print("b is highest")
else:
    print("c is highest")

x = int(input("please enter the value : "))
if x<0:
    print("x is negative")
elif x>0:
    print("x is positive number")
elif x == 0:
    print("x is equal to zero")

total = int(input("please enter the value of x: "))
if(total<100):
    total=total+20
elif(total>=100 and total<=200):
    total = total + 100
else:
    total = total + 00
print(total)
print("total=" + str(total))        # we cant concantenate string and int. need to convert int to str
print(f'{"total value"}{total}')    # "f-string" can be used to displayed str with int


