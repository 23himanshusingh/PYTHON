'''py
x=[]
for i in range(4):
    y=[]
    for j in range(4):
        if i==2 and j==2:
            a='@'
        else:
            a=i+1
        y.append(a)
    x.append(y)
for i in range(4):
    for j in range(4):
        print(x[i][j],end=' ')
    print() 
'''