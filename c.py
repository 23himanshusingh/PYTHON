n=int(input("enter po"))
l1,l2,l3=[],[],[]
for i in range(n):
    str1=str(input("enter co"))
l1.append(str1.split())

for i in range (len(l1)):
    l2.append(l1[i][0])
    l3.append(l1[i][0])
count1,count2=0,0
for i in range (len(l2)):
    if l2.count(l2[i])>1:
        count1=(l2.count(l1[i]))-1
for i in range(len(l3)):
    if l3.count(l2[i])>1:
        count2=(l3.count(l2[i]))-1

print(count1,count2)



