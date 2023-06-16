s=input()
l=s.strip().split()
t=""
# print(l)
f,x=0,0
for i in range(len(l)):
    k=l[i].strip().find("[")
    if k!=-1 and k!=0:
        k1=l[i].strip().find("]")
        j1=ord(l[i][k-1])
        if (j1>=97 and j1<=122) or (j1>=65 and j1<=122):
            snew=l[i][:k]
            snew1=snew[::-1]
            for j in snew1:
                while j.isalpha():
                    t=t+j
            print(t+" "+l[i][k+1:k1])
            f+=1
            t=""
# print(f)
if f==0:
    print("-1")