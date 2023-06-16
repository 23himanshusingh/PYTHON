n=int(input());l=[]
for i in range(n):
    l.append(int(input()))
c,s=0,0;li=[]
for i in range(len(l)-1):
    if s<10:
        s=s+(li[i]+li[i+1])
        if s>=10:
            s=0
            c+=1
        else:
            continue
    else:
        s=0
        c+=1


