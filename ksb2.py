

# int tag;
# int* factors(int n)
# {
#     int a[1000000];
#     for(int i=1;i<=n/2;i++)
#         if(n%i==0)
#             a[++tag]=i;
#     a[++tag]=n;
#     return(a);
# }
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
t=int(input())
for z in range(1,t+1):
# A Better (than Naive) Solution to find all divisors



    n=int(input())
    a=printDivisors(n);cnt=0
    for i in range(len(a)):
        if str(a[i])==str(a[i])[::-1]:
            cnt+=1
    print("Case #{}: {}".format(z,cnt))


