s=input();l=[];start,end=0,len(s)//3
for i in range(start,end):
    l.append(s[start:end])
    start,end=end,end+len(s)//3
if len(set(l))==1:
    print("YES")
else:
    print("NO")
print(set([1,2,3,3,4])) 

