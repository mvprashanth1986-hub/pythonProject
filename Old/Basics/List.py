score = [10,20,30,40,50]
alpha = ["aaa","bbb","ccc"]
print(alpha)
print(score)
print(score[1]) #prints value based on given index
print(score[-1])    #prints value based on given index counting reversly
print(score[:])     #prints all the values
print(score + [1,2,3])          #Concantination
print(score + ['a','b','c'])

score[2] = 100      #edit the values and provide the new value for the list
print(score)

number = [1,2,3,4,5]
print(number)
number.append(100)  #adds the value at the end
print(number)

name = ['a','b','c','d']
print(name)
name[2:4] = []      #adds the value based on the range specified
print(name)

test = [10,20,30,40,50]
print(len(test))

a = [1,2,3]
n = ['a','b','c']
print(a)
print(n)
x = [a,n]       #saves the values of a and n in to new list x as a group
print(x)
print(len(x))
print(x[1][2])      #prints the value based on index inside index