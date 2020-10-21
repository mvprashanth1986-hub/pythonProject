# list = [1,2,3,4,5]
# print(list)
# count = len(list)
# temp = list[0]
# list[0] = list[count-1]
# list[count-1] = temp
# print(list)

# list[0],list[count-1]=list[count-1],list[0]
# print(list)

list = [1,2,3,4,5]
start,*middle,end = list

print(start)
print(middle)
print(end)