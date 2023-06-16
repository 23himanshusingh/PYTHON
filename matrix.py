y=[]
c=int(input("c"))
r=int(input("r"))
for i in range(1,r+1):
    x=[]
    for j in range(1,c+1):
        n=5*((i+j)**2)
        x.append(n)
    y.append(x)
# print(y)
for i in y:
    print(*i)





