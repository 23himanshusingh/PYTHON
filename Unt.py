from _typeshed import WriteableBuffer


n=int(input())#size of array
l=list(map(int,input().split()[:n]))#inputting array elements
# traversing in the elements within the array list
for i in range(len(l)-1):
    if l[i]>l[i+1]:# checking if right most adjacent element is smaller or not
        l[i]=l[i+1]
    else:
        l[i]=-1

l[len(l)-1]=-1
# print(l)
l=map(str,l)
s=' '.join(l)
print(s)





s=input()
li=list(set(s))
li.sort()
f=[]
for i in li:
    c=s.count(i)
    f.append(c)
print(li,f)
lis,f1=[],[]

max=f[0]
for i in range(len(f)):
    for j in range(len(f)):
        if f[j]>=max:
            max=f[j]
            
    f.remove(f[k])
    lis.append(li[k])
    f1.append(f[k])
print(lis,f1)


