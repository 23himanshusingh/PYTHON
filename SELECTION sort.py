l=list(map(int,input().split()))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            l[j],l[i]=l[i],l[j]
            
    print(l)
print(l)