import re

str = "I am a student of http://www.automationtool.com/ and even also fan of http://www.python.com"
url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)

print(url)