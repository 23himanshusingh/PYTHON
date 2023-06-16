s=input("name=")
l=list(s)
l1=['a','e','i','o','u']
for i in range(len(l)):
    if l[i] in l1:
        l[i]=chr(ord(l[i])+1)
print(l)
print(''.join(l))


n=int(input())
n=int(input())
a=int(input())
b=int(input())
m=max(a,b)
n=min(a,b)
p1=m+m+n
p2=m+n+n
print(p1,p2,m,n)
c,t=0,0
if p1==n:
    c+=1
elif p2==n:
    t+=1
else:
    print('Cannot be written')
if c==1:
    print(m)
    print(n)
 

