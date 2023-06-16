n=int(input())
x=2;li=[];c=0
while True:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        li.append(x)
        c+=1
    if c==n:
        break
    else:
        x+=1
print(li)



