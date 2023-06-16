def reverse_triangle1(n):
    ans=[]
    for i in range(n):
        lis=[]
        for j in range(i,n):
            lis.append('*')
        for j in range(i+1):
            lis.append(' ')
        ans.append(lis)
    return ans
def reverse_triangle2(n):
    ans=[]
    for i in range(n):
        lis=[]
        for j in range(i):
            lis.append(' ')
        for j in range(i,n):
            lis.append('*')
        ans.append(lis)
    return ans
a1=reverse_triangle1(5)
a2=reverse_triangle2(5)

y=[]
for i in range(len(a1)):
    x=a1[i]+a2[i]
    y.append(x)
z=y[::-1]
for i in range(1,len(z)):
    y.append(z[i])

for i in y:
    for j in i:
        print(j,end='')
    print()





