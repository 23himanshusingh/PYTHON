n=int(input());x=[]
for i in range(n):
    x.append(int(input()))
x=tuple(x);l=len(x);ans=[]
for i in range(l-1):
    for j in range(i+1,l):
        if x[i]<=x[j]:
            break
        else:
            continue
    else:
        ans.append(x[i])
ans.append(x[l-1])
print(ans)