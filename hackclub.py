n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i+1,n):
        if (l[i]+l[j])%4==0:
            c=c+1
print(c)