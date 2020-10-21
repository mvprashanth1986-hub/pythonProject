a = [1,2,3,4,5,1000]
sum = 0
count = len(a)

for i in range(0,count):
    sum = sum + a[i]

print(sum)

print(sum(a))
print(sum(a,100))