a = [1,2,100,500,3,4,5]
# print(a)
# print(min(a))
# print(max(a))

max=a[0]
n = len(a)

for i in range(1,n):
    if a[i] > max:
        max = a[i]
print(max)


min=a[0]
n = len(a)
for i in range(1,n):
    if a[i] < min:
        min = a[i]
print(min)