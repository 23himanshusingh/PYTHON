n=sorted(input())
l=[];l2=[]
for i in n:
    l2.append(n.count(i))
    l2.sort(reverse=True)
    
    
res=[]

for i in l2:
    for j in n:
        if i==n.count(j):
            l.append([j,i])
print(l)        
print(list(set([1,2,3,4,2222,2,3,4])))


for i in l: 

    if i not in res: 

        res.append(i)



for i in res:
    print(*i)

    



    



