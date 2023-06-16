# n=int(input());li=[]
# for i in range(n):
    # li.append(input())

def make(i):
    l=['d','f'];r=['j','k'];s,r1=2,2;time=[]
    for ch in i:
        if ch in l:
            r1=2
            time.append(s)
            s=4
        if ch in r:
            s=2
            time.append(r1)
            r1=4
    return sum(time)
li=[]
n=int(input())
for i in range(n):
    li.append(input())
d={}
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
# print(d)
d1={}
for i in set(li):
    a=make(i)
    d1[i]=a
# print(d1)
for i in d1:
    d1[i]+=(d[i]-1)*d1[i]//2
# print(d1)
print(sum(list(d1.values())))
        
            
            
            