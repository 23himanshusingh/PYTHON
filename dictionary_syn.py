d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60};d={}
d.update(d1)
d.update(d2)
d.update(d3)
print(d)
'''or we can use ** which allows multiple arguments to be passed to a function'''
#eg
def merge(d1,d2,d3):
    res={**d1,**d2,**d3}
    return res
print(merge(d1,d2,d3))
dict={1:2}
print(dict)
d1=dict.fromkeys([1,2,3,4],"o")
d1.popitem()
print(d1)

# Python code to demonstrate working of
# has_key() and get()
  
# Initializing dictionary
d= { 'Name' : 'Nandini', 'Age' : 19 }
  
# using has_key() to check if dic1 has a key
if d.has_key('Name'):
       print ("Name is a key")
else : print ("Name is not a key")


# Python code to demonstrate working of
# setdefault()

# Python code to demonstrate working of
# setdefault()
  
# Initializing dictionary
dict = { 'Name' : 'Nandini', 'Age' : 19 }
  
# using setdefault() to print a key value
print ("The value associated with Age is : ",end="")
print (dict.setdefault('A'))
  
# printing dictionary values
print ("The dictionary values are : ")
print (str(dict))
print(list(dict.items()))
print(type(dict))
di={chr(k):k for k in range(ord("a"),ord("c"))}
for i,j in list(di.items()):
    print(i,j)
from collections import OrderedDict
d=OrderedDict()
print(d)
print(list({0:1,"hw":2}))
list(d.setdefault(chr(k), k) for k in range(ord('a'), ord('g')))
print(list(d))

