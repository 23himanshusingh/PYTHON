n=int(input());x=[]
for i in range(n):
    y=[]
    for j in range(3):
        a=int(input())
        if a<0 or a>255:
            print("error")
        else:
            y.append(a)
    x.append(y)
for i in range(n):
    if i%2==0:
        x[i][0]=255-x[i][0]
    else:
        x[i][2]=255-x[i][2]
lis=[]      
for i in x:
    if i not in lis:
        lis.append(i)
print(lis);ma=[];mi=[]
for i in lis:
    ma.append(max(i))
    mi.append(min(i))
maxv=max(ma);c1=0
minv=min(mi);c2=0
for i in lis:
    for j in i:
        if j==maxv:
            c1+=1
        if j==minv:
            c2+=1
d={}
d[minv]=c2;d[maxv]=c1
print(d)



