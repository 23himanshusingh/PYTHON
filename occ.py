def fruit(l):
    lis=[]
    for i in l:
        if l.count(i)>=2:
            lis.append(i)
    return 
li=[]
for i in range(5):
    li.append(input())
print(fruit(li))
