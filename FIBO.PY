from math import*
n=input()
l=[];l1=[]
for i in range(len(n)):
    for j in range(len(n)):
      a=n[i:i+j+1]
      l.append(int(a))
for i in set(l):
    b=5*(i**2)+4
    c=5*(i**2)-4
    d=sqrt(b)
    e=sqrt(c)
    if ceil(d)==floor(d) or ceil(e)==floor(e):
        l1.append(i)
if len(l1)==0:
    print('None')
s=sorted(l1)
for i in s:
    print(i)