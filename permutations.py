'''lis=list(input())
print(lis)
from itertools import permutations
for i in range(1,len(lis)+1):
    for j in permutations(lis,i):
        j=list(j)
        print(''.join(j))'''
lis=list("1234")

from itertools import permutations
for i in permutations(lis,4):
    print(i)

