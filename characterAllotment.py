w=input()
n=int(input())
l=len(w)
x=n//l
s=w*x
y=n-len(s)
s1=w[:y]
p=[]

for i in s:
    p.append(i)
for i in s1:
    p.append(i)
s2=w[y:]
s3=s2+s
j=-1
for i in range(n-1,-1,-1):
    j+=1
    if (s3[j]==p[i]):
        print(i+1)
        break
else:
    print(-1)
    