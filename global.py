def func():
    global lis
    lis=[2,4,6]
    return lis
lis=[1,2,3]
print(lis)
print(func())
print(lis)


def myFun(x):
 
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x=x+[3]
    x=x+[1]
    print(x)
 
 
# Driver Code (Note that lst is not modified
# after function call.
x = [10,11]
myFun(x)
print(x)

def f(s):
    s+='q'
    print("Inside Function", s)
 
# Global scope
s = "I love Geeksforgeeks"
print(s)
f(s)
print("Outside Function", s)