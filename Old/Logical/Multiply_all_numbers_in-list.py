#Approach1
list = [1,3,2,4,5]

final = 1
for i in list:
    final = final * i

print(final)

#Approach2
import numpy

list = [2,3,5,10]
result = numpy.prod(list)
print(result)