#num = int(input("Please enter the number :  "))
# num = 6
# fact = 1

# if num<0:
#     print("Factorial does not exist for negative numbers")
# elif num==0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         fact = fact * i
#     print("Factorial f ",num, " is ", fact)

def fact(n):
    if (n==0 or n==0):
        return 1
    else:
        return n * fact(n-1)

n = 5
f = fact(n)
print(f)