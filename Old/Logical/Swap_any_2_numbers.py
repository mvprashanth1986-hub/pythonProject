list = [10,20,50,60]
print(list)
pos1,pos2 = 1,3
list[pos1],list[pos2] = list[pos2],list[pos1]
print(list)