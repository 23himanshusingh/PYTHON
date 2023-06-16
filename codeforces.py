# cook your dish here
for t in range(int(input())):
    n=int(input());ans=[]
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        flag=False;mini=1000011
        for j in range(i,n):
            x=(a[i]+b[j])%n
            if x==0:
                flag=True
                break
            else:
                if mini>x:
                    mini=x;pos=j
                else:
                    continue
        if flag:
            ans.append(0)
            continue
        else:
            ans.append(mini)
            b[i],b[pos]=b[pos],b[i]
    print(*ans)



