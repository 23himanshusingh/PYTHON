s1=input()
s2=input()
import re
if (re.match(r'\d+',s1) and re.match(r'\d+',s2)) or (re.match(r'[A-Za-z]',s2) and re.match(r'[A-Za-z]',s1)) or (re.match(r'[A-Za-z]+[0-9]+',s1) and re.match(r'[0-9]+[A-Za-z]+',s2) or):
    def subseq(s):
        from itertools import combinations
        l1=[]
        for i in range(1,len(s)+1):
            for c in combinations(s,i):
                l1.append(list(c))
        l2=[]
        for i in l1:
            l2.append(''.join(i))
        return l2
    st=subseq(s2)
    if s1 in st:
        print('true')
    else:
        print('false')
else:
    print('invalid')


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
        return 0
    if any(f>1 for f in c.values()):
        max=c.most_common(1);lis=[]
        lis=sorted(a,key=a.count,reverse=True)
        count=0
        for i in lis:
            if i!=max:
                lis[0]+i
                count+=1
            lis=lis.append(lis[1])
            count=count+1
        return count

    else:
        return -1
t=int(input())
for i in range(t):
    print(nested(int(input())))

```py
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
        return 0
    if any(f>1 for f in c.values()):
        max=c.most_common(1)
        return n-max[0][1]+1
    else:
        return -1
t=int(input())
for i in range(t):
    print(nested(int(input())))```


