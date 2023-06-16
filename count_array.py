st=sorted(input());d={}
for i in range(len(st)):
    if st[i] not in d:
        d[st[i]]=1
    else:
        d[st[i]]+=1
print(d)
ans=sorted(list(d.keys()),key=lambda k:d[k],reverse=True)
print(ans)


