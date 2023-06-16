from itertools import permutations
n=int(input())
l,li=[],[]
for i in range(n):
    l.append(input())
def lexi(str):
    from itertools import permutations
    ans=[]
    lis=list(str)
    for perm in permutations(lis,len(lis)):
        s=''.join(list(perm))
        ans.append(s)
    ans=sorted(ans)
    return ans
print(lexi("aabccdf"))
ansf=[]
for i in l:
    ansf.append(lexi(i))
for i in ansf:
    print(i)
