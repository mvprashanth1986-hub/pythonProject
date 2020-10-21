num1 = 10
num2 = 20

num1 = input("please enter the first value")
num2 = input("please enter the second value")

print(num1,num2)
temp = num1
num1= num2
num2 = temp
print(num1,num2)

num1,num2 = num2,num1

print(num1,num2)