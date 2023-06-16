b=[];x=1
n=int(input())
for i in range(2,n+1):
    if i%2==0:
        x=x^i
        b.append(x)
    else:
        x=x&i
        b.append(x)
print(b)