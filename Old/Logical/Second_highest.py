#Approach2

list = [10,30,10,80,40,60,70,50]
temp = set(list)
temp.remove(max(temp))

print(max(temp))