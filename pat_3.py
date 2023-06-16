n=int(input());l=[];import sys
if n==0:
    print("no students visited")
    sys.exit()
else:
    for i in range(n):
        l.append(input())
    li=set(l)
    print(li)
    r=input()
    c=0
    for i in li:
        if i==r:
            print("found")
            c+=1
    if c==0:
        print("not found")
print(min({"hello","world"}))