d={}
for i in range(6):
    state=input()
    districts=int(input())
    d[state]=districts
dis=d.values()
st=d.keys()
l1=[];c1=[];elements_their_count=[]
for i in dis:
    if i not in l1:
        l1.append(i)
print(l1)
for i in l1:
    c=0
    for j in dis:
        if i==j:
            c+=1
            c1.append(c)
print(l1,c1)
for i in range(len(c1)):
    o=[l1[i],c1[i]]
    elements_their_count.append(o)
elements_their_count=sorted(elements_their_count,key=lambda x:int(x[1]),reverse=True)
y,z=[],[]
for i in range(len(elements_their_count)):
    if elements_their_count[i][1]==elements_their_count[0][1]:
        y.append(elements_their_count[i][1])
        z.append(elements_their_count[i][0])


final={}
for i in z:
    lis=[]
    for j in dis:
        if d.get(j)==i:
            lis.append(j)
            h=z.index(i)
    final[y[h]]=lis
print(final)








