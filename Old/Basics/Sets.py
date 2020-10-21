#It ignores the dulplicate
#It saves different data types
#It performs different mathematical operations
#It doesnot store duplicate items
#No indexing and it prints the values randomly
s1 = {1,2,3,4}
print(s1)
s2 = {'James',20,300,'Bond'}
s3 = set("python")
print(s3)
s4 = set([10,20,30,40,50,60,70,80,90,100])
print(s4)

#While creating set object, you store Numbers,strins,tuple

s4 = {10,20,30,40}
s5 = {30,40,50,60}
print(s4|s5)            #Union of two sets
print(s4.union(s5))     #Union of two sets

print(s4&s5)            #Intersection
print(s4.intersection(s5))  #Intersection

print(s4-s5)                #Difference
print(s4.difference(s5))    #Difference

print(s4^s5)
print(s4.symmetric_difference(s5))      #Symmetric Values (values from both sets excluding common values)

s10 = {"Java","Python","Ruby"}
s10.add("Perl")                     #Adding values
print(s10)

s10.update(["C","VBA"])             #Adding list values
print(s10)

s10.update(("HTML","C++"))          #Adding Tuple values
print(s10)

s11 = s10.copy()        #Duplicating Values
print(s11)

s11.discard("Java")
print(s11)

s11.remove("Python")
print(s11)




