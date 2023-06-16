from itertools import *
s='ABCD'
n=len(s)
res1=''
res2=sorted([s[i:j] for i,j in combinations(range(n+1),2)],key=lambda x: len(x))

for i in range(1,n+1):
    res1+=' '.join([''.join(j) for j in list(combinations(s,i))])+' '

print('String :',s)
print('Subsequence :',res1)
print('Substring :',*res2)
# another way
'''import itertools
 
def Sub_Sequences(STR):
    combs = []
    for l in range(1, len(STR)+1):
        combs.append(list(itertools.combinations(STR, l)))
    for c in combs:
        for t in c:
            print (''.join(t), end =' ')'''
