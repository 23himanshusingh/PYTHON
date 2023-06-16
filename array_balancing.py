t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x,y=a[0],b[0]
    s=0
    for i in range(1,n):
        sum1=abs(a[i]-x)+abs(b[i]-y)
        sum2=abs(b[i]-x)+abs(a[i]-y)
        if sum1<sum2:
            x=a[i]
            y=b[i]
            s+=sum1
        else:
            x=b[i]
            y=a[i]
            s+=sum2
    print(s)