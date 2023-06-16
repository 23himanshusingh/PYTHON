n=int(input());d={}
import sys
for i in range(n):
    l=list(map(int,input().split()))
    for i in l[1:]:
        if i<=0:
            print("invalid")
            sys.exit()
    d[l[0]]=set(l[1:])
value=list(d.values())
d1={}
for i in range(len(value)-1):
    for j in range(i+1,len(value)):
        li=[]
        v1=value[i]&value[j]
        d1[(i,j)]=v1
# print(d1.items())
final=sorted(d1.items(), key =lambda kv:len(kv[1]),reverse=True)
# print(list(final[0]))
f=list(final[0]) 
ans=[]
for i in f:
    ans.append(list(i))
# print(ans)
leng=len(ans[1])
if leng!=0:
    for i in ans[0]:
        print(i+1,end=" ")
    print()
    print(*ans[1])
    print(leng)
else:
    print("NO winner")























