n=int(input("no"))
c,i,s=1,0,0
if n>0:
    while c<=n:
        while True:
            i+=1
            if i%2==0:
                break
            else:
                if c<=n-1:
                    print(i,"",end="")
                    s=s+i
                if c==n:
                    print(i)
                    s=s+i
                c+=1
if n>0:
    print(s)
    print("invalid")

print("hhdssdfhsdjf")



