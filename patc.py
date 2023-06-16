import math
 
 
def isPerfectSquare(x):
 
    #if x >= 0,
    if(x >= 0):
        sr = math.sqrt(x)
        # sqrt function returns floating value so we have to convert it into integer
        #return boolean T/F
        return ((sr*sr) == float(x))
    return False
 
# Driver code
 
 
if (isPerfectSquare(int(input()))):
    print("Yes")
else:
    print("No")


