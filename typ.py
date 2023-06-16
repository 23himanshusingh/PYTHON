l=[i for i in range(1,16)]
from itertools import combinations
li=[]
for i,j in combinations(l,2):
    if i+j==15: 
        li.append([i,j])
        li.append([j,i])
print(li)