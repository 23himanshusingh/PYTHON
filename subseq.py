# s1='abcd'= a b c d ab ac ad abc acd bc bcd bd cd abcd 
from itertools import combinations
s=input();l1=[]
for c in combinations(s,):
    l1.append(list(c))
l2=[]
for i in l1:
    l2.append(''.join(i))
print(l2)
