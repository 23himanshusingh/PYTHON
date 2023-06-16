n=int(input("size: "))
l=list(map(int,input().split()[:n]))
for i in range(n):
    if i==(n-1):
        l[i]=-1
    elif l[i]>l[i+1]:
        l[i]=l[i+1]
for i in range(n):
    l[i]=str(l[i])
print(" ".join(l))


n1=input()
n2=input()
l=[]
l4=[]
l3=[]
l1=[]
l2=[]
for i in n1:
    l1.append(i)
for i in n2:
    l2.append(i)

for i in range(len(n2),0,-1):
    a=(10**i)/10
    l.append(int(a))

for i in range(len(n1)):
     if l1[i]==l2[i]:
        l3.append(l1[i])

print(l3)
if len(l3)==0:
    print('No digits are same')
else:       
  for i in l3:
    a=l1.index(i)
    l4.append(a)
  l4.reverse()

  for i in l4:
    pos=l[i]
    if l[i]==1:
        print("Same at 1's position"%1)
    else:
      print("Same at %dth position"%pos)


