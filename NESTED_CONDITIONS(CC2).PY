def nested(n):
    a=list(map(int,input().split()))
    from collections import Counter
    c=Counter(a)
    
    if len(a)==1:
        return 0
    if (len(set(a))==1 and len(a)>2):
        return 0 
    if len(a)==2 and a[0]!=a[1]:
        return -1
    if len(a)==2 and a[0]==a[1]:
        return 1
    if any(f>1 for f in c.values()):
        max=c.most_common(1)
        return n-max[0][1]+1
    else:
        return -1
t=int(input())
for i in range(t):
    print(nested(int(input())))


