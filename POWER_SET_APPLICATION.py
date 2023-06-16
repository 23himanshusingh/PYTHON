x,n=int(input()),int(input())
arr=list(map(int,input().split()))
for i in range((2**n)-1):
    l=[];l1=[]
    for j in range(n):
        if (i & (1<<j))!=0:
            l.append(arr[j])
            l1.append(j+1)
    if sum(l)==x and len(l)==4:
        print(*l1)
        break
else:
    print("No")
