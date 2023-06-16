n=int(input())
m=int(input())
k=0
def funct(j,n):
    c=0
    if ((10**n)+1)%j==0:
        c+=1
    return c
for j in range(2,m+1):
    if funct(j,n)==1:
        print(j)
        k+=1
if k==0:
    print("No complete factors")






n=int(input())
m=int(input())
c=0
k=0
def funct(j,n):
    c=0
    for i in range(10**(n-1),10**n):
        i=str(i)
        i1=i+i
        i1=int(i1)
        if i1%j==0:
            c+=1
        else:
            break
    return c
for j in range(2,m+1):
    if funct(j,n)==9*(10**(n-1)):
        print(j,"",end="")
        k+=1
if k==0:
    print("No complete factors")