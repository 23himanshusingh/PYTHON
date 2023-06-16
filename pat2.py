n=int(input())
num=n
s=0
if n<0:
    print("Invalid input")
else:
    n=str(n)
    l=len(n)
    if l!=1:
        n=int(n)
        while n>0:
            d=n%10
            s=s+d**3
            q=n//10
            n=q
        if(s==num):
            print("equal")
        else:
            print("unequal")
    else:
        print("Do not enter single digit")
