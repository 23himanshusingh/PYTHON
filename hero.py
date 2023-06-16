s=input()
l=s.split()
print(l)


# print(l)
f=0
for i in range(len(l)):
    for o in l[i]:
        if o=="[":
            k=l[i].index(o)
    
        if k!=0:
            if l[i][k-1].isalpha():
                k1=l[i].find("]")
                t=""
                snew=l[i][:k]
                snew1=snew[::-1]
                print(snew,snew1)
                counter=0
                for j in snew1:
                    if j.isalpha():
                        counter+=1
                        t=t+j
                    else:
                        break
                if counter!=0:   
                    print(t[::-1]+" "+l[i][k+1:k1])
                    f=f+1
        else:
            print(func(l[i],k+1))

            
# print(f)
if f==0:
    print("-1")





