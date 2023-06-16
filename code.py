'''def solve(x):
    from itertools import combinations as c
    l=[i for i in range(1,1001)]
    for i in c(l,3):
        s=sum(i)
        mean=s/3
        if mean==float(x):
            print(*list(i))
            break'''
from itertools import combinations_with_replacement as c
t=int(input())
for i in range(t):
    n,k,x=map(int,input().split())
    if k<x:
        print(-1)
        continue
    else:
        j=0
        for i in range(n):
            print(j%x,end=' ')
            j+=1
        print()
        

