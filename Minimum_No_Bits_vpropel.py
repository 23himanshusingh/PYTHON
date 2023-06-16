import math
n=int(input())
arr=list(map(int,input().split()))
m=max(arr)
print((math.floor(math.log(m,2))+1))