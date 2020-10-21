import re

str = "Hi I am learning Python automation<>}"
regex = re.compile("<>*()_+|}{:")
flag = regex.search(str)

print(flag)

