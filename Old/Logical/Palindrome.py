s = input("Please enter the string :  ")
print(s)

print(s[:])
print(s[0:5])
print(s[0:5:1])
print(s[::])
rev = s[::-1]
print(rev)

if s == rev:
    print("String is palindrome")
else:
    print("String is not palindrome")