n=int(input())
lis=input().split()
print(lis)
x=[]
for i in range(len(lis)):
    y=[]
    for ch in lis[i]:
        ind=lis[i].index(ch)
        if ind==0:
            st=(ch*int(ch))+lis[i][ind+1:]
        elif ind==len(lis[i])-1:
            st=lis[i][:ind]+ch*int(ch)
        else:
            st=lis[i][:ind]+ch*int(ch)+lis[i][ind+1:]
        y.append(int(st))
    x.append(y)
print(x);li=[]
for i in x:
    a=max(i)
    li.append(a)
print(sorted(li))


    