t=int(input())
from collections import Counter as c
for z in range(1,t+1):
    n,d=map(int,input().split())
    arr=list(map(int,input().split()))
    a=c(arr)
    if a['1']<a['0']:
        print("Case #{}: {}".format(z,a['1']+1))
    elif a['1']>a['0']:
        print("Case #{}: {}".format(z,a['0']+1))
    else:
        print("Case #{}: {}".format(z,a['0']-1))
    print(a)
        
    