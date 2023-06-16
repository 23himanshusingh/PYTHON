n=int(input());l=[]
for i in range(n):
    l.append(int(input()))
c,s=0,0;li=[]
for i in range(len(l)-1):
    if s+l[i]<10:
        s=s+l[i]
        if s==10:
            c+=1
            s=0
            continue
        if s>10:
            i=i-1
            s=0
            c+=1
            continue
    elif s+l[i]==10:
        s=0
        c+=1
        continue
    else:
        s=0
        c+=1
        continue
print(c+2)




