s = input()
l1 = []
l2 = []
for i in s:
    l2.append(i)
    l1.append(s.count(i))
z = list(zip(l1,l2))

r1 = list(set(z))
r1.sort(reverse=True)
r1=list(map(list,r1))
print(r1)
for i in range(len(r1)-1):
    if r1[i][0]==r1[i+1][0]:
        if ord(r1[i][1])>ord(r1[i+1][1]):
            r1[i][1],r1[i+1][1]=r1[i+1][1],r1[i][1]
for i in range(len(r1)):
    print(r1[i][1],r1[i][0])
    



    



