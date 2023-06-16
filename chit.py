import copy
m,n,p,q=int(input()),int(input()),int(input()),int(input())
chit=[];ans=[]
for i in range(m):
    l=list(map(int,input().split()))
    chit.append(l)
lis=copy.deepcopy(chit)
lucky=int(input())
if lucky==p:
    for i in range(m):
        for j in range(n):
            if lis[i][j]==p:
                r=i;c=j
                if any(lis[r][j]==q for j in range(n)) or any(lis[i][c]==q for i in range(m)):
                    chit[r][j]=q
    for i in range(m):
        for j in range(n):
            if chit[i][j]==p:
                ans.append([i+1,j+1])
else:
    for i in range(m):
        for j in range(n):
            if lis[i][j]==q:
                r=i;c=j
                if any(lis[r][j]==p for j in range(n)) or any(lis[i][c]==p for i in range(m)):
                    chit[r][j]=p
                    ans.append([r,c])
    for i in range(m):
        for j in range(n):
            if chit[i][j]==p:
                ans.append([i+1,j+1])
import sys
if len(ans)==0:
    print("No winner")
    sys.exit()
ansf=sorted(ans);from collections import OrderedDict
d=OrderedDict()
for i in range(len(ansf)):
    if ansf[i][0] not in d:
        d[ansf[i][0]]=[ansf[i][1]]
    else:
        d[ansf[i][0]].append(ansf[i][1])
final=[]
for key in d:
    d[key].sort()
    for i in d[key]:
        final.append((key,i))
        
for i,j in final:
    print(i,j)
    
    


