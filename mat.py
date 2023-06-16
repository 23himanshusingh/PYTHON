n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(l);li=[]
for i in l:
    if i%3==0 and i%5==0:
        li.append("three five")
    elif i%3==0 and i%5!=0:
        li.append("three")
    elif i%3!=0 and i%5==0:
        li.append("five")
    else:
        li.append(i)
print(tuple(li))



d={1:3,2:4}
for x,y in d.

