amt=int(input())
ans=[]
n=int(input())
for i in range(n):
    l,b,c=map(int,input().split())
    if amt<=c:
        ans.append([l,b,c])
if ans:
    for i in range(len(ans)):
        for j in range(i+1,len(ans)):
            x1,y1,z1=ans[i]
            x2,y2,z2=ans[j]
            if x1*y1 > x2*y2 :
                temp = ans[i]
                ans[i]=ans[j]
                ans[j]=temp
    print(*ans[i])
else:
    print("No")