w1=input()[::-1]
w2=input()[::-1]
a="abcdefghijklmnopqrstuvwxyz"
c=0
z=""
for i,j in zip(w1,w2):
    s=str(ord(i)+ord(j)+c)
    z+=s[-1]
    c=int(s[0:-1])
l=len(w1)-len(w2)
if l>0:
    for i in w1[-l:]:
        s=str(ord(i)+c)
        z+=s[-1]
        c=int(s[0:-1])
if l<0:
    for i in w2[l:]:
        s=str(ord(i)+c)
        z+=s[-1]
        c=int(s[0:-1])
z+=str(c)[::-1]
print(z[::-1])
ans=""
for i in z[:-2]:
    ans+=a[int(i)]
i=int(z[-2::][::-1])
while i>25:
    i-=26
ans+=a[i]
print(ans[::-1])