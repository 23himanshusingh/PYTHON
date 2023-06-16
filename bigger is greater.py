w=input()
l=list(w);ans=[]
from itertools import permutations as p
for perm in p(l,len(w)):

    ans.append(''.join(list(perm)))
ans=list(set(ans))
ans.sort()
ind=ans.index(w)
print(ans)