str = 'welcome to python programming'

words = str.split(" ")
print(words)
rev_words = words[-1::-1]
print(rev_words)
rev_string = ' ' .join(rev_words)

print(rev_string)