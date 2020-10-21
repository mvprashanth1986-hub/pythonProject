#Approach1
str = "Hello Wrold !!!!"

count=0
for i in str:
    count = count + 1

print(count)
print(len(str))

#Approach2
count = 0
while str[count:]:
    count = count + 1

print(count)

#Approach3
str1 = 'X'
str2 = str1.join(str).count(str1)
print(str2)



