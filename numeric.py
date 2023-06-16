m=int(input());x=[]
for i in range(m):
    y=[]
    for j in range(m):
        a=int(input())
        y.append(a)
    x.append(y)
c1=False;c2=False
for i in range(m):
    for j in range(m):
        if i!=j and x[i][j]!=0:
            c1=False
            break
        else:
            c1=True
for i in range(m):
    for j in range(m):
        if i==j and x[i][j]%2==0:
            c2=True
        else:
            c2=False
            break
if c1 and c2:
    print("Diagonals_Even")
else:
    print("Diagonals_NotEven")


