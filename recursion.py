def f(i,l,n,x,sum,arr):
    if (i==n):
        if len(l)==x:
            if(sum%2!=0):
                print(*l)
                return 1
            else:
                return 0
        else:
            return 0
    l.append(arr[i])
    sum+=arr[i]
    if (f(i+1,l,n,x,sum,arr)==1):
        return 1
    sum-=arr[i]
    l.pop()
    if (f(i+1,l,n,x,sum,arr)==1):
        return 1
    return 0
t=int(input())
for i in range(t):
    l=[]
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    if f(0,l,n,x,0,arr):
        print("YES")
    else:
        print("NO")





