'''eg forgeeksskeegfor the output=geeksskeeg'''
st=input();l=len(st);lis=[]
for i in range(l):
    for j in range(i+1,l+1):
        if st[i:j]==st[i:j][::-1]:
            lis.append(st[i:j])
print(sorted(lis,key=lambda x:len(x),reverse=True)[0])
