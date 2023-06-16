r1=int(input())
c1=int(input())
m1,m2=[],[]
for i in range(r1):
    y=list(map(int,input().split()))
    m1.append(y)
r2=int(input())
c2=int(input())
for i in range(r2):
    z=list(map(int,input().split()))
    m2.append(z)
m3=[]
for i in m1:
    lis=[]
    for j in i:
        if any(j in x for x in m2):
            lis.append(0)
        else:
            lis.append(j)
    m3.append(lis)
# print(m3)
for i in m3:
    for j in i:
        print(j,end=' ')
    print()