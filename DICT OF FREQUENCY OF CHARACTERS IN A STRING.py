'''input=bbbccddaaadefffghhf
output={'f': 4, 'b': 3, 'd': 3, 'a': 3, 'c': 2, 'h': 2, 'e': 1, 'g': 1}'''
'''METHOD 1 :from collections import Counter
inp="bbbccddaaadefffghhf"
print(Counter(inp))
print(C'''
'''METHOD 2:'''
from collections import OrderedDict
inp=sorted(input());d=OrderedDict()
for i in inp:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
lis=list(d.items());ans=[]
for i in lis:
    ans.append(list(i))
ansfinal=sorted(ans,key=lambda x:-x[1])
ansfinal1=ansfinal[:3]
for i in ansfinal1:
    print(*i)
'''Input : test_str = ‘geekforgeeks’
Output : [‘r’, ‘o’, ‘f’, ‘s’]'''
odd_freq_char=[]
for key in d:
    if d[key]%2!=0:
        odd_freq_char.append(key)
print(odd_freq_char)


