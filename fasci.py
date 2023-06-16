s = str(input())
b = int(input())
l1 = []
l2 = []
for i in s:
    l2.append(i)
    l1.append(s.count(i))
z = list(zip(l1,l2))

r1 = list(set(z))
r1.sort(reverse=True)
r1=r1[:b]
r1=list(map(list,r1))
print(r1)
max=r1[0]
for i in r1:
    if 


