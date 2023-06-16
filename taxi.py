n=int(input())
size=list(map(int,input().split()))

size.sort()

cab=0
while len(size)>1:
    s=size[0]+size[-1]
    if s>4:
        size.pop(-1)
        cab+=1
    elif s==4:
        size.pop(0)
        size.pop()
        cab+=1
    else:
        size.append(size.pop(0)+size.pop(-1))
if len(size)>0:
    cab+=1
print(cab)
        
        
        
print(hex(10))
s1="j"
s2="f"
s2,s1=s1,s2
print(s1,s2)