# A Better (than Naive) Solution to find all divisors
import math
 
# method to print the divisors
def printDivisors(n) :
    res=[]
     
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                # print (i,end=" ")
                res.append(i)
            else :
                # Otherwise print both
                # print (i , int(n/i), end=" ")
                res.append(i)
                res.append(int(n/i))
        i = i + 1
    return res
