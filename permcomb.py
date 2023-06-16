
def permutations(head, tail=''):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i]  + head[i+1:], tail + head[i])
```py
from itertools import permutations
n=int(input());lis=[];l=[1,2]
for i in range(1,n+1):
    for perm in permutations(l*i,i):
        lis.append(perm)
count=0
for i in set(lis):
    if sum(i)==n:
        count+=1
print(count%(10**7 + 7))

        
       



