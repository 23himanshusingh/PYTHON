a=input();l=[];l1=[];c1=[];elements_their_count=[]
for i in a:
    if i not in l1:
        l1.append(i)
for i in l1:
    c=0
    for j in a: 
       if i==j:
          c=c+1
    c1.append(c)
for i in range(len(c1)):
    o=[l1[i],c1[i]]
    elements_their_count.append(o)
elements_their_count=sorted(elements_their_count,key=lambda x:x[0])
elements_their_count=sorted(elements_their_count,key=lambda x:int(x[1])reverse=True)
lis=elements_their_count[:3]
for i in lis:
    print(*i)
