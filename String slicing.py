name="himanshu"
print(name[3]) # accessing a character in string
# name[3] = "e"--->does not work
print(type(name[3]))

print(name[0:8]) # prints first 8 characters of string "himanshu"
print(name[2:5]) # prints man ie characters from index 2 to 4,the index in strings start from 0 to (length-1) in PYTHON
print(name[1:]) # is same as name[1:8]
print(name[:4]) # is same as name[0:4]

# negative indices
print(name[-1]);print(name[-8])
b='singh'
print(b[-5:-1]) # is same as name[0:4] 