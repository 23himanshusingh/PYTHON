n=int(input("no"))
num=n
c=0
k=0
rev=0
while n>0:
    d=n%10
    if d==0:
        k=k+1
    rev=rev*10+d
    q=n//10
    n=q
    c=c+1
    if c==2:
        break

rev1=0
l=0
if k==2:
    print('Division cannot be performed')
    l=l+1
else:
    while rev>0:
        d1=rev%10
        rev1=rev1*10+d1
        q1=rev//10
        rev=q1
if l==0:
    print(num%rev1)
    rev=q1

  

