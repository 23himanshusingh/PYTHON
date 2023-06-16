l=[[6,7],[8,7],[5,4]]
c=6
# print(any(3==i[0] for i in l ))
if not any(c==i[0] for i in l) and not any(c==i[1] for i in l):
    print(0)
print(any(c==i[0] for i in l))
print(any(c==i[1] for i in l))
ans=[]
ans.clear()
'''4
4 6
6 7
8 7'''