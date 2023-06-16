n=int(input())
c,m=0,1
if n==2 or n==3:
    print("Cannot be decided")
else:
    while (6*m-1)<=n or (6*m+1)<=n:
        if n==(6*m+1) or n==(6*m-1):
            print("Cannot be decided")
            c+=1
        if c==1:
            break
        m+=1
if c==0 and n!=2 and n!=3:
    print("Composite number")

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


m=int(input(" m"))
n=int(input(" n"))
i=1
j=1
c=0
l1=[]
l2=[]
c1=0
while i<31:
    i=i+m
    l1.append(i)
    c1+=1

while j<31:    
    j=j+n
    l2.append(j)
    
for i in range(len(l1)):
    if l1[i] in l2:
        c+=1
print(c+1)
    
    
    