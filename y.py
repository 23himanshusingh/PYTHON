n=int(input())
c=0
number=n
while n>0:
    d=n%10
    if d==0:
        continue
    if number%d==0:
        c=c+1
        print(d)
    q=n//10
    n=q
if c==0:
    print("no")