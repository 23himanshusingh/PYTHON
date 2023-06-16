n=int(input("pin"))
num=n
s=str(n)
l=len(s)
rev=0
if l==4:
    n=int(s)
    while n>0:
        d=n%10
        rev=rev*10+d
        q=n//10
        n=q
        snew=""

    while rev>0:
        d1=rev%10
        newd1=(d1+7)%10
        newd1=str(newd1)
        snew=newd1+snew
        q1=rev//10
        rev=q1
  
    final=snew[2:3]+snew[3:4]+snew[0:1]+snew[1:2]
    print(final)
else:
    print('invalid')

print(math.ceil(7.4))

l1=[101,102,13]
l1.sort()
l1.reverse()
l2=l1.copy()
print(l2)
