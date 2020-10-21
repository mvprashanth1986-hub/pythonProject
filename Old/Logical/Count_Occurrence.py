#Approach2
list = [2, 5, 7, 2, 1, 6, 4, 2, 2, 4, 5]
x = 2
count = 0

for i in list:
    if(i==x):
        count = count + 1

print("{} ha occured {} times".format(x,count))