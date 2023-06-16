n=int(input());l=[]
for i in range(n):
    l.append(int(input()))
c=0;li=[]
for i in range(len(l)-1):
    if sum(li)+l[i+1]<10:
        li.append(l[i])
        if sum(li)>=10:
            li=[]
            c+=1
            continue
        continue
print(c+1)