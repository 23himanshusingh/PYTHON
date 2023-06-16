
s=input()
f=[]
s1=''
for i in s:
    if i not in s1:
        s1+=i
ch=list(s1)
for i in s1:
    f.append(s.count(i))
d=list(zip(ch,f))
d.sort()
print(dict(d))
l=[1,2,3]
print(l[0:2])
aabbbccde
b 3
a 2
c 2
e 1
d 1

    li=[]
    for i in range(len(arr)):
        if i==0:
            if sum(arr[1:]):
                li.append(arr[i])
                
        if i==len(arr)-1:
            if sum(arr[:len(arr)-1])==0:
                li.append(arr[i])
        if i!=0 and i!=len(arr)-1:
            if sum(arr[:i])==sum(arr[i+1:]):
                li.append(arr[i])
    print(li)
    if len(li)!=0:
        return "YES"
    else:
        return "NO"
print(len([]))

n=input()
l=[]
for i in n:
    l.append([i,n.count(i)])
    
res=[]


for i in l: 

    if i not in res: 

        res.append(i)



for i in res:
    print(*i)


