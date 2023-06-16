n=int(input())
l=list(map(int,input().split()[:n]));li=[];ind=[]
for i in range(len(l)):
    if l[i]>=0:
        ind.append(i)
        li.append(l[i])
li.sort();ind.sort()
j=0
for i in ind:
    l[i]=li[j]
    j+=1
l=list(map(str,l))
print(" ".join(l))




