name = ["java","python","dot net","c sharp"]

for i in name:
    print(i)

str = "This is Python code of the year"

for i in str:
    print((i+i)*5)

list = ["python", "automation", "labs"]

for i in range(len(list)):
    print(list[i])

list1 = ["India","USA","Japan","NY","LA","Perth"]

for index in range(len(list1)):
    print(list1[index])
else:
    print("out of bound")

list2 = ["India", "USA", "Japan", "NY", "LA", "Perth"]

for index in range(len(list2)):
    print(list2[index])
else:
    print("out of bound")

for i in range(1,5):
    for j in range(i):
        print(i)