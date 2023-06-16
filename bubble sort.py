n=int(input());lis=[]
for i in range(n):
    lis.append(int(input()))
count=1
while count<n:
    for i in range(n-count):
        if lis[i]>lis[i+1]:
            lis[i],lis[i+1]=lis[i+1],lis[i]
    count+=1
print(*lis)