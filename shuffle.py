for a0 in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    final=[]
    for i in range(n):
        cond=True
        y=0
        f=0
        while cond and y<n+1:
            if n+y-a[i] in b:
                final.append(y)
                b.remove(n+y-a[i])
                cond=False
            elif y-a[i] in b:
                final.append(y)
                b.remove(y-a[i])
                cond=False
            y+=1
    print(*final)