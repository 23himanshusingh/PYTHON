def perm(n):
    lis=[i for i in range(1,n+1)]
    li=[];from itertools import permutations
    for i in permutations(lis,n):
        li.append(list(i))
    return li
print(perm(3))
def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists[1:]
def good(l):
    ok=0
    for i in sub_lists(l):
        l=l.index(i[0])
        r=l.index(i[-1])
        p=(r+1)-(l+1)+1
        perms=perm(p)
        for i in perms:
            if any(i==j for j in sub_lists(l)):
                ok=ok+1
    if ok:
        return True
    else:
        return False



t=int(input())
for i in range(t):
    n,k=map(int,input().split()))
    lists=perm(n)
    sub
