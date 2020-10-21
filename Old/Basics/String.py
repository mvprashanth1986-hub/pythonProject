s1 = 'Hello World'
s2 = "Hello India"

print(s1,"\n\n\n\n\n",s2)  #new line escape character
print(s1,"\t\t",s2)     #Tab escape character
print(s1[0])    #Index of string
print(s1[1])
print(s1+s2)    #concantination
print(s1+"  "+s2)
print(s2*5)         #prints string 5 times
print(s1[0:8])      #prints characters for the range specified
print("test" in s1)     #prints true/false
print("java" not in s1)     #prints true/false


#printing paragraph
s3 = """This is automation demo             
This is the completion of pytest series
the next series will be API testing"""

print(s3)
#printing paragraph
s4='''This is the paragraph
we will display the paragraph in different lines
This is the end of paragraph'''

print(s4)

str1 = "THIS IS THE PYTHON CODE AND I LOVE CODING. lets see after full stop"  #Only capitalizes first letter
print(str1.capitalize())        #Only capitalizes first letter
print(str1.count("CO"))     #Counts the number of occurances
print(str1.find("THE"))     #Returns the position of the sub string
print(len(str1))            #Returns the number of characters present in the string

str2= "  z  hello    "
print(str2.lstrip())        #Removes space in lift side
print(str2.rstrip())        #REmoves spce in right side
print(max(str2))            #prints Z
print(min(str2))            #prints a
print(str2.replace("hello","good"))     #replaces the text

str6 = "Java hello python hello robot"

str8 = str6.split("hello")      #splits string based on the substring and saves as list
print(str8)
print(str8[0])

st = "Python"
print(st[5])
print(st[-2])       #prints the character counting from reverse

a = "test"
b = "test"

print(a is b)

str = 'Python is a programming language'    #Returns True/False if the string has aphanumeric
print (str.isalnum())
str = 'ThisisInterviewQuestion17'
print (str.isalnum())